# Slider Trinkey firmware

CircuitPython firmware for the Adafruit Slider Trinkey. It reads the slide potentiometer and prints the position over USB serial for the CAD A11y viewer. Install steps are in [docs/slider.md](../../docs/slider.md).

## Status

`code.py` is not here yet. It will be the code running on the sliders in use.

## What the firmware must do

The viewer reads lines from the board's USB serial port. Each line is `Slider: ` followed by a number from 0 to 100, ending in a newline:

```text
Slider: 0
Slider: 42
Slider: 100
```

The details of how the viewer reads these lines are in [docs/slider.md](../../docs/slider.md#serial-format).

## Pinning versions

Record the versions the firmware was tested with when you add or change it:

- CircuitPython: 10.3.1 is the current stable release.
- Adafruit CircuitPython Bundle: the release you copied libraries from, for example `20260930`.

Put the libraries `code.py` imports in a `lib` folder here, copied from the bundle that matches the CircuitPython major version. Don't rely on `circup` to reproduce them: it ignores version pins in `requirements.txt` and always installs from the newest bundle.

## Licensing

The firmware is BSD-3-Clause, like the rest of the code here. Two exceptions:

- If `code.py` is based on an Adafruit Learning System example, keep the SPDX copyright and license lines at its top, which name Adafruit and the MIT license. Then run `reuse download MIT` so the MIT text is in `LICENSES/`.
- The compiled libraries in `lib` cannot hold a header. Add an annotation for `firmware/slider-trinkey/lib/**` to `REUSE.toml` with Adafruit's copyright and the MIT license.
