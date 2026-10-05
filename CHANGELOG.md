# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
For the hardware, a new major version means a change that breaks older builds:
a printed part that no longer fits the previous ones, or a different face-to-view map.

## [Unreleased]

## [0.1.0] - 2026-10-05

### Added
*   Parts lists for the orientation cube and the slider, each with a column describing how to tell the part apart by touch.
*   The slider's CircuitPython firmware, as it runs on the sliders in use. It only needs CircuitPython's built-in modules.
*   Guides to connecting and using the cube and the slider, written so every step can be followed without images, and an archive page for the first cube, the Tactile ViewCube.
*   The cube's Onshape source, recorded in `hardware/cube/onshape.toml`. Exports are only accepted from a named Onshape version, and a check on every pull request confirms each file matches its checksum.
*   The cube's design, version v0.1.0, as STEP and Parasolid files in `hardware/cube`. The cube prints as two halves, `upper_cube` and `lower_cube`. The source is now a maintainer's copy of Felix Hähnlein's Onshape document, with a CERN-OHL-P-2.0 license tab.
*   Print files go on the GitHub release instead of in the repository, because the meshes are large: one STL per half and a 3MF with both. The export check rejects STL and 3MF files under `hardware/`.
*   Licenses declared with REUSE: CERN-OHL-P-2.0 for the hardware designs and parts lists, and the University of Washington's BSD-3-Clause license for everything else. Also citation and Open Know-How metadata.

[Unreleased]: https://github.com/cad-accessibility/tangible-controls/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/cad-accessibility/tangible-controls/releases/tag/v0.1.0
