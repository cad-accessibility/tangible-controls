# tangible-controls

Hand-held controls for [CAD A11y](https://github.com/cad-accessibility/cad-a11y), an accessible 3D model viewer for blind and low-vision people. This repository holds the designs, parts lists, firmware and build instructions, so anyone can make the devices, use them, and change them.

The instructions do not depend on images. Each step can be followed with a screen reader, and the parts lists say how to tell parts apart by touch.

## The devices

| Device | What it does | Status |
| --- | --- | --- |
| [Orientation cube](docs/cube.md) | Turn a face of the cube up to switch the viewer to that standard view. It is a WitMotion WT901BLECL motion sensor inside a 3D-printed cube. | Parts list and use guide are ready. Print files and assembly steps are not published yet. |
| [Slider](docs/slider.md) | Slide the knob to set the slice depth. It is an Adafruit Slider Trinkey running CircuitPython. | Parts list and setup guide are ready. The firmware is not here yet. |
| [Tactile ViewCube](docs/gen1-viewcube.md) | The first cube, built around a GoDice die. | Archived. |

Both devices need Chrome or Edge, because the viewer reaches them through Web Bluetooth and Web Serial.

## What is where

- `bom/`: parts lists, one CSV file per device.
- `docs/`: build, setup and use guides, and the maintainers' guide to [exporting from Onshape](docs/export-from-onshape.md).
- `firmware/`: CircuitPython firmware for the slider.
- `hardware/`: CAD exports, one folder per device, each with a manifest that names its Onshape source.
- `scripts/`: the checks that run on every pull request.
- `LICENSES/`: the full text of each license.

## The CAD

The cube is designed in Onshape, in the document [cube final](https://cad.onshape.com/documents/bacc1f6ed9ff69f796727760/w/9e219d2c0ee1db9e9269d6d5) by Felix Hähnlein. Files under `hardware/` are exported from named Onshape versions, which cannot be changed afterwards, so each release points to the exact geometry it contains. You do not need Onshape to print or inspect the parts.

## Licenses

Two licenses apply, declared file by file with [REUSE](https://reuse.software/) in `REUSE.toml`:

- Hardware designs and parts lists (`hardware/`, `bom/`): [CERN-OHL-P-2.0](LICENSES/CERN-OHL-P-2.0.txt), the permissive CERN Open Hardware Licence.
- Everything else, code and documentation: [BSD-3-Clause](LICENSES/BSD-3-Clause.txt), the University of Washington license that cad-a11y and a11yhood use.

Copyright 2026 University of Washington.

## Citing

If you use these devices in research, cite them with the details in [CITATION.cff](CITATION.cff). On GitHub, "Cite this repository" in the About section gives the same citation in APA and BibTeX.

## Contributing

Bug reports, build reports and accessibility problems are welcome as issues. [CONTRIBUTING.md](CONTRIBUTING.md) explains how to make a change, and [GOVERNANCE.md](GOVERNANCE.md) explains who reviews and merges it.

## Credits

Felix Hähnlein designed both cubes. The drivers were written in cad-a11y by Felix Hähnlein, Carlos E. Tejada and Jennifer Mankoff. Carlos E. Tejada maintains this repository. CAD A11y is developed at the University of Washington's Center for Research and Education on Accessible Technology and Experiences (CREATE), with support from the National Science Foundation.
