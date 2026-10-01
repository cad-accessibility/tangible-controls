# Exporting the CAD from Onshape

This page is for maintainers. The cube is designed in Onshape, which has no file you can commit that keeps the design's feature history. So for each device this repository keeps three things:

1. **A link to the Onshape document.** It is the source for anyone who wants to change the design.
2. **Exports of one named Onshape version**, so people can print or inspect the design without Onshape.
3. **A manifest and checksums** that tie each export to that version: `onshape.toml` and `SHA256SUMS` in the device's folder under `hardware/`.

Onshape versions cannot be edited or deleted, so a version link always opens the geometry that was exported. A workspace link, with `/w/` in it, shows the live design, which can change at any time. `scripts/check_exports.py` runs on every pull request and fails if an export is not listed in the manifest, if exports are listed without a version, or if a file does not match its checksum.

## Before the first export

The document owner does these once, in Onshape.

1. **Add a license tab, before creating any version,** so every version carries it. Under Onshape's Terms of Use, a public document whose owner is not on the Free plan keeps the terms set in a tab named LICENSE. Import a plain text file with this notice, which is the one CERN recommends, and name its tab `LICENSE`:

   ```text
   Copyright 2026 University of Washington.

   This source describes Open Hardware and is licensed under the CERN-OHL-P v2.

   You may redistribute and modify this documentation and make products using it under the terms of the CERN-OHL-P v2 (https://cern.ch/cern-ohl). This documentation is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-P v2 for applicable conditions.

   Full licence text: https://spdx.org/licenses/CERN-OHL-P-2.0.html
   Exported files: https://github.com/cad-accessibility/tangible-controls
   ```

2. **Allow exports.** In the Share dialog, make the document public, so anyone with an Onshape account can copy and change the source, and in Link sharing check "Allow exporting from the link". Today the cube's link lets people view the design but not export it.

## Each release

1. Finish the changes in the Onshape workspace.
2. Create a version in the Version and history panel. Name it after the release, for example `v0.2.0`.
3. Open that version. Its URL contains `/v/` followed by 24 characters: that is the version ID.
4. From the version, export each printed part, in millimeters, in these formats:
   - **Parasolid** (`.x_t`): Onshape's own geometry format, and the most faithful copy of the design outside Onshape.
   - **STEP** (`.step`): opens in almost any CAD program.
   - **STL** (`.stl`): what slicers read. Add **3MF** (`.3mf`) as well if you have it.
5. Name each file after its part, in lowercase with hyphens, for example `cube-shell.step`. Put the files in the device's folder, such as `hardware/cube/`.
6. In that folder's `onshape.toml`, add or replace the `[version]` table, and add one `[[export]]` table per file:

   ```toml
   [version]
   name = "v0.2.0"
   id = "the 24 characters after /v/"
   created = 2026-10-05

   [[export]]
   file = "cube-shell.step"
   element = "cube_final"
   part = "the part's name in Onshape"
   ```

   `element` must match the name of an `[[element]]` table in the same file.
7. Write the checksums:

   ```sh
   python3 scripts/check_exports.py --write-sums hardware/cube
   ```

8. Check the whole repository. It should end with "No problems".

   ```sh
   python3 scripts/check_exports.py
   ```

9. If anything changed for people building the cube, update the BOM, the build docs and `CHANGELOG.md`.
10. Open a pull request, and put the version's `/v/` link in its description.

## Reviewing a CAD change

- In Onshape, compare the new version with the previous one in the Version and history panel.
- GitHub shows STL files in a 3D viewer, including a before and after view in pull requests. That view is visual only, so the pull request description must also say in words what changed: which part, which dimensions, and why.
- The checks confirm the files match the manifest. They cannot confirm that the part prints and fits, so someone has to print it before the release.

## Why this is not automated

The Onshape API can export from a version, and tools such as [onshape-to-robot](https://onshape-to-robot.readthedocs.io/) accept a version ID. But it needs an API key tied to one person's Onshape account, which can have at most two keys, and Free, Standard and student Education accounts are limited to 2,500 API calls a year. For one small part released a few times a year, exporting by hand and letting CI check the checksums is less to maintain. Revisit this if the design gains configurations or frequent releases.
