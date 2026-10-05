# Hardware

Each folder here holds one device's design, exported from Onshape.

- [cube](cube/onshape.toml): the orientation cube, version v0.1.0, as `cube.step` and `cube.x_t` (Parasolid). The cube prints as two halves, `upper_cube` and `lower_cube`.

Every folder has an `onshape.toml` that names the Onshape document, its Part Studios and the version the files were exported from, and a `SHA256SUMS` file for those files. How to export and update them is in [docs/export-from-onshape.md](../docs/export-from-onshape.md).

Print files are not kept here. The STL and 3MF meshes are large, so they are attached to the [GitHub release](https://github.com/cad-accessibility/tangible-controls/releases) with the same name as the Onshape version.

The designs in this folder are licensed under the CERN Open Hardware Licence Version 2, Permissive ([CERN-OHL-P-2.0](../LICENSES/CERN-OHL-P-2.0.txt)). Copyright 2026 University of Washington.
