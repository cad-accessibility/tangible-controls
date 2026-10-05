# Exporting the CAD from Onshape

This page is for maintainers. The cube is designed in Onshape, which has no file you can commit that keeps the design's feature history. So for each device this repository keeps:

1. **A link to the Onshape document.** It is the source for anyone who wants to change the design.
2. **STEP and Parasolid exports of one named Onshape version**, in the device's folder under `hardware/`, so people can inspect or modify the design without Onshape.
3. **A manifest and checksums** that tie each export to that version: `onshape.toml` and `SHA256SUMS` in the same folder.
4. **Print files on the GitHub release.** STL and 3MF meshes are large, so they are attached to the release with the same name as the Onshape version instead of being committed. Releases are immutable, and GitHub lists a SHA-256 for each file.

Onshape versions cannot be edited or deleted, so a version link always opens the geometry that was exported. A workspace link, with `/w/` in it, shows the live design, which can change at any time. `scripts/check_exports.py` runs on every pull request. It fails if an export is not listed in the manifest, if exports are listed without a version, if a file does not match its checksum, or if an STL or 3MF file is committed.

## The cube's Onshape document

The source is [tangible-controls cube](https://cad.onshape.com/documents/3ceaf96421d57106502c1ab5), owned by a maintainer. It is a copy of Felix Hähnlein's original document, "cube final", made on 2026-10-05 so the source does not depend on one person's account. `hardware/cube/onshape.toml` records both.

Only the owner, or someone the owner shares the document with as "Can edit" with Share, Export and Delete, can do everything on this page. Onshape needs Delete to create versions and Share to change sharing. Before the owner leaves the project, they transfer the document to another maintainer, as GOVERNANCE.md says.

## Before the first export

The owner does these once, in Onshape.

1. **Add a license tab, before creating any version,** so every version carries it. Under Onshape's Terms of Use, a public document whose owner is not on the Free plan keeps the terms set in a tab named LICENSE. Import a plain text file with this notice, which is the one CERN recommends, then rename its tab to `LICENSE`:

   ```text
   Copyright 2026 University of Washington.
   Designed by Felix Hähnlein. Original document: https://cad.onshape.com/documents/bacc1f6ed9ff69f796727760

   This source describes Open Hardware and is licensed under the CERN-OHL-P v2.

   You may redistribute and modify this documentation and make products using it under the terms of the CERN-OHL-P v2 (https://cern.ch/cern-ohl). This documentation is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-P v2 for applicable conditions.

   Full licence text: https://spdx.org/licenses/CERN-OHL-P-2.0.html
   Exported files: https://github.com/cad-accessibility/tangible-controls
   ```

2. **Make the document public.** In the Share dialog's Public tab, select "Make public". Anyone signed in to Onshape can then find, view and copy it.
3. **Turn on link sharing, then allow exports.** In the Link sharing tab, select "Turn on link sharing" first, and then check "Allow exporting from the link". People without an Onshape account can then open the link and export from it.

## Each release

1. Finish the changes in the Onshape workspace.
2. Create a version in the Versions and history panel, with the pin-and-plus icon at the top of the panel or by right-clicking the workspace row. Name it after the release, for example `v0.2.0`.
3. Right-click the version and choose "Open". Its URL now contains `/v/` followed by 24 characters: that is the version ID. Export everything from this view.
4. In the Part Studio, select the printed parts and export them. In a view-only window, use the export button in the bottom toolbar and choose "Select and export...", select the parts in the Parts list, and press Return to confirm. Export these formats:
   - **Parasolid**, both parts in one file. Onshape's own geometry format, and the most faithful copy of the design outside Onshape.
   - **STEP**, both parts in one file, with "Use custom units for export" set to Millimeter. It opens in almost any CAD program. Onshape prepares it as a translation, so the download arrives a few seconds after the others.
   - **STL** for the release, with "Export unique parts as individual files" checked, Binary, Millimeter, Fine. One file per part.
   - **3MF** for the release, both parts in one file, Fine. Onshape writes 3MF in meters and records that unit in the file, so say so in the release notes and point people to the STL files, which are in millimeters.
5. Put the Parasolid and STEP files in the device's folder as `<device>.x_t` and `<device>.step`, for example `hardware/cube/cube.step`. Never commit the STL or 3MF files; the check rejects them.
6. In that folder's `onshape.toml`, replace the `[version]` table and the `[[export]]` tables:

   ```toml
   [version]
   name = "v0.2.0"
   id = "the 24 characters after /v/"
   created = 2026-10-05
   url = "https://cad.onshape.com/documents/<document id>/v/<version id>"

   [[export]]
   file = "cube.step"
   format = "STEP AP242, millimeters"
   element = "cube_final"
   parts = ["upper_cube", "lower_cube"]
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
11. After it merges, create the GitHub release `v0.2.0` as a draft, attach the STL and 3MF files, check them, and publish it.

## Reviewing a CAD change

- In Onshape, compare the new version with the previous one in the Versions and history panel.
- The pull request description must say in words what changed: which part, which dimensions, and why. Any render or screenshot needs alt text that says the same.
- The checks confirm the files match the manifest. They cannot confirm that the part prints and fits, so someone has to print it before the release.

## Why this is not automated

The Onshape API can export from a version, and tools such as [onshape-to-robot](https://onshape-to-robot.readthedocs.io/) accept a version ID. But the export endpoints need an API key tied to one person's Onshape account, even when link sharing allows exports, and that account can have at most two keys. Free, Standard and student Education accounts are also limited to 2,500 API calls a year. For one small part released a few times a year, exporting by hand and letting CI check the checksums is less to maintain. Revisit this if the design gains configurations or frequent releases.
