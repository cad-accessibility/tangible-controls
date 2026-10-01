# Generation 1: the Tactile ViewCube (archived)

Before the WitMotion cube, Felix Hähnlein's Tactile ViewCube held a GoDice, a Bluetooth die made by Particula. The die reported which number was on top, and the CAD A11y server turned that into a view. cad-a11y removed the GoDice code in June 2026, in [pull request #32](https://github.com/cad-accessibility/cad-a11y/pull/32), when the WitMotion cube replaced it.

This page is a record. Nothing for Generation 1 is maintained, and its print files are not in this repository.

## Face map

| Die face on top | View |
| --- | --- |
| 1 | z- |
| 2 | y- |
| 3 | x- |
| 4 | x+ |
| 5 | y+ |
| 6 | z+ |

## Putting the die in the cube

These are Felix's instructions from November 2025.

1. Charge the GoDice with its charger for about 10 seconds. The charging contacts are on the 5 face.
2. Put the die in the ViewCube with the 3 face toward the round nubbin and the 6 face up.
3. Close the ViewCube.

## Where the code is

The Generation 1 code is in cad-a11y's history:

- `app/server.py` in the parent of commit `401d796`: the last and cleanest version, which ran the GoDice connection in the server.
- `utils_dice.py` in commit `594ed4c`: the GoDice helpers.
- `server_cube.py` in commit `7e57ec7`, and `server_cube_slider.py` in commit `2a7938d`: earlier standalone servers.

The GoDice Python library is `godice` on PyPI, from Particula's [GoDicePythonAPI](https://github.com/ParticulaCode/GoDicePythonAPI) repository. Check its license before reusing or redistributing any of this code.
