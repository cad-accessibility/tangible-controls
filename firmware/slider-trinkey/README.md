# Slider Trinkey firmware

CircuitPython firmware for the Adafruit Slider Trinkey. It reads the slide potentiometer and prints the position over USB serial for the CAD A11y viewer. Install steps are in [docs/slider.md](../../docs/slider.md).

## Status

[code.py](code.py) is the code that runs on the sliders in use, kept exactly as it runs there. The CircuitPython version it was tested with is not recorded yet.

## What it does

Every 0.1 seconds it reads the potentiometer, whose raw value runs from 0 to 65535, scales it to 0 to 100, and prints `Slider: ` followed by that number. When it starts, it also prints the raw reading once on a line of its own, which the viewer ignores.

## What the viewer expects

The viewer reads lines from the board's USB serial port. It uses each line that starts with `Slider: ` followed by a number from 0 to 100, and ignores every other line. The details are in [docs/slider.md](../../docs/slider.md#serial-format).

## Libraries and versions

`code.py` only uses modules built into CircuitPython (`board`, `analogio` and `time`), so there is no `lib` folder to copy and no library versions to pin.

When you test a change, record the CircuitPython version here. 10.3.1 is the current stable release.

If a later version imports an Adafruit library, put it in a `lib` folder here, copied from the Adafruit CircuitPython Bundle release that matches the CircuitPython major version, and record both versions. Don't rely on `circup` to reproduce them: it ignores version pins in `requirements.txt` and always installs from the newest bundle.

## Licensing

The firmware is BSD-3-Clause, like the rest of the code here. Two cases need more:

- Code based on an Adafruit Learning System example keeps the SPDX copyright and license lines at its top, which name Adafruit and the MIT license. Then run `reuse download MIT` so the MIT text is in `LICENSES/`.
- Compiled libraries in a `lib` folder cannot hold a header. Give `firmware/slider-trinkey/lib/**` an annotation in `REUSE.toml` with Adafruit's copyright and the MIT license.
