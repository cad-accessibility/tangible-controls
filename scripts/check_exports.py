#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 University of Washington
# SPDX-License-Identifier: BSD-3-Clause
"""Check that every CAD export in hardware/ comes from a named Onshape version.

Each device folder under hardware/ has an onshape.toml that says which Onshape
document, Part Studios and version its files were exported from. For every
folder this script checks that:

- the manifest names the document and its Part Studios by their Onshape IDs;
- exports are listed only when the manifest names an Onshape version;
- every CAD file in the folder is listed as an export, and every listed
  export exists;
- SHA256SUMS lists exactly the exports, and every checksum matches.

It also rejects CAD files anywhere under hardware/ that sit outside a folder
with a manifest.

Run it from anywhere in the repository:

    python3 scripts/check_exports.py
    python3 scripts/check_exports.py --write-sums hardware/cube

--write-sums rewrites one folder's SHA256SUMS from the exports its manifest
lists, then checks that folder. Python 3.11 or later, standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HARDWARE = ROOT / "hardware"
MANIFEST = "onshape.toml"
SUMS = "SHA256SUMS"
CAD_SUFFIXES = {".step", ".stp", ".x_t", ".x_b", ".stl", ".3mf"}
ONSHAPE_ID = re.compile(r"[0-9a-f]{24}")
SUM_LINE = re.compile(r"([0-9a-f]{64}) [ *](.+)")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_onshape_id(value: object) -> bool:
    return isinstance(value, str) and ONSHAPE_ID.fullmatch(value) is not None


def read_manifest(folder: Path) -> dict:
    return tomllib.loads((folder / MANIFEST).read_text(encoding="utf-8"))


def listed_exports(manifest: dict) -> list[str]:
    return [str(export.get("file", "")) for export in manifest.get("export", [])]


def is_plain_name(name: str) -> bool:
    return bool(name) and "/" not in name and "\\" not in name and not name.startswith(".")


def read_sums(path: Path) -> dict[str, str]:
    sums: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        match = SUM_LINE.fullmatch(line)
        if match is None:
            raise ValueError(f"line {number} is not '<sha256>  <file name>'")
        sums[match.group(2)] = match.group(1)
    return sums


def check_folder(folder: Path) -> list[str]:
    rel = folder.relative_to(ROOT).as_posix()
    problems: list[str] = []

    try:
        manifest = read_manifest(folder)
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as err:
        return [f"{rel}/{MANIFEST}: cannot read it: {err}"]

    document = manifest.get("document", {})
    if not is_onshape_id(document.get("id")):
        problems.append(f"{rel}/{MANIFEST}: [document] id must be 24 lowercase hex characters.")

    elements: dict[str, dict] = {}
    for element in manifest.get("element", []):
        name = str(element.get("name", ""))
        if not name:
            problems.append(f"{rel}/{MANIFEST}: an [[element]] has no name.")
        elif not is_onshape_id(element.get("id")):
            problems.append(f"{rel}/{MANIFEST}: element {name!r} id must be 24 lowercase hex characters.")
        elements[name] = element

    version = manifest.get("version")
    if version is not None:
        if not version.get("name"):
            problems.append(f"{rel}/{MANIFEST}: [version] needs the version's name as shown in Onshape.")
        if not is_onshape_id(version.get("id")):
            problems.append(f"{rel}/{MANIFEST}: [version] id must be the 24 hex characters after /v/ in the version's URL.")

    listed = listed_exports(manifest)
    if listed and version is None:
        problems.append(
            f"{rel}/{MANIFEST}: exports are listed but there is no [version]. "
            "Export from a named Onshape version, not from the workspace."
        )
    if len(set(listed)) != len(listed):
        problems.append(f"{rel}/{MANIFEST}: an export file is listed more than once.")

    exports: list[str] = []
    for export in manifest.get("export", []):
        name = str(export.get("file", ""))
        if not is_plain_name(name):
            problems.append(f"{rel}/{MANIFEST}: export file {name!r} must be a plain file name in this folder.")
            continue
        exports.append(name)
        if Path(name).suffix.lower() not in CAD_SUFFIXES:
            problems.append(f"{rel}/{MANIFEST}: export {name!r} is not a CAD file ({', '.join(sorted(CAD_SUFFIXES))}).")
        if export.get("element") not in elements:
            problems.append(f"{rel}/{MANIFEST}: export {name!r} names element {export.get('element')!r}, which is not an [[element]].")
        if not (folder / name).is_file():
            problems.append(f"{rel}/{name}: listed as an export but the file is missing.")

    on_disk = {p.name for p in folder.iterdir() if p.is_file() and p.suffix.lower() in CAD_SUFFIXES}
    for name in sorted(on_disk - set(exports)):
        problems.append(f"{rel}/{name}: CAD file is not listed as an export in {MANIFEST}.")

    sums_path = folder / SUMS
    if exports and not sums_path.is_file():
        problems.append(f"{rel}: {SUMS} is missing. Run: python3 scripts/check_exports.py --write-sums {rel}")
    elif sums_path.is_file():
        try:
            sums = read_sums(sums_path)
        except (OSError, UnicodeDecodeError, ValueError) as err:
            problems.append(f"{rel}/{SUMS}: {err}")
        else:
            for name in sorted(set(sums) - set(exports)):
                problems.append(f"{rel}/{SUMS}: lists {name}, which is not an export in {MANIFEST}.")
            for name in sorted(set(exports) - set(sums)):
                problems.append(f"{rel}/{SUMS}: has no checksum for {name}.")
            for name in sorted(set(exports) & set(sums)):
                path = folder / name
                if path.is_file() and sha256(path) != sums[name]:
                    problems.append(
                        f"{rel}/{name}: does not match its checksum in {SUMS}. "
                        "Export it again from the pinned version, or run --write-sums "
                        "if you exported a new version on purpose."
                    )

    return problems


def stray_cad_files() -> list[str]:
    problems = []
    for path in sorted(HARDWARE.rglob("*")):
        if path.is_file() and path.suffix.lower() in CAD_SUFFIXES and not (path.parent / MANIFEST).is_file():
            rel = path.relative_to(ROOT).as_posix()
            problems.append(f"{rel}: CAD file in a folder without {MANIFEST}.")
    return problems


def write_sums(folder: Path) -> list[str]:
    rel = folder.relative_to(ROOT).as_posix()
    try:
        exports = listed_exports(read_manifest(folder))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as err:
        return [f"{rel}/{MANIFEST}: cannot read it: {err}"]
    bad = [name for name in exports if not is_plain_name(name)]
    if bad:
        return [f"{rel}/{MANIFEST}: export file {name!r} must be a plain file name in this folder." for name in bad]
    missing = [name for name in exports if not (folder / name).is_file()]
    if missing:
        return [f"{rel}/{name}: listed as an export but the file is missing." for name in missing]
    lines = [f"{sha256(folder / name)}  {name}\n" for name in sorted(exports)]
    (folder / SUMS).write_text("".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote {rel}/{SUMS} with {len(lines)} checksum(s).")
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--write-sums",
        metavar="FOLDER",
        type=Path,
        help="rewrite FOLDER/SHA256SUMS from the exports its onshape.toml lists, then check it",
    )
    args = parser.parse_args()

    if args.write_sums is not None:
        folder = args.write_sums.resolve()
        if folder.parent != HARDWARE or not (folder / MANIFEST).is_file():
            print(f"{args.write_sums}: not a device folder under hardware/ with an {MANIFEST}.")
            return 2
        problems = write_sums(folder) or check_folder(folder)
        folders = [folder]
    else:
        folders = sorted(p.parent for p in HARDWARE.glob(f"*/{MANIFEST}"))
        problems = stray_cad_files()
        for folder in folders:
            problems.extend(check_folder(folder))

    for problem in problems:
        print(problem)
    if problems:
        print(f"{len(problems)} problem(s) found.")
        return 1
    print(f"No problems in {len(folders)} hardware folder(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
