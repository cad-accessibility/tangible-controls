# The slider

The slider is an Adafruit Slider Trinkey: a small circuit board with a slide knob and a USB plug. Moving the knob sets the slice depth in the CAD A11y viewer, from 0 to 100 percent.

## Status

- **Parts** are listed in [bom/slider.csv](../bom/slider.csv).
- **The firmware is not in this repository yet.** It will be the `code.py` that runs on the sliders in use. See [firmware/slider-trinkey](../firmware/slider-trinkey/README.md).
- **The printed bed** that the original instructions mention, which holds the board so it is easier to handle, is not in this repository yet.

## What you need

- The parts in [bom/slider.csv](../bom/slider.csv).
- A computer with Chrome or Edge. The viewer reads the slider over Web Serial, which Firefox and Safari do not support.

## Install CircuitPython

You only need to do this once per board.

1. Plug the board into a USB port. Use a port, cable or adapter that carries data.
2. Double-click the board's reset button. Its lights turn green and a drive named TRINKEYBOOT appears.
3. Download the CircuitPython file for the Slider Trinkey from [circuitpython.org/board/adafruit_slide_trinkey_m0](https://circuitpython.org/board/adafruit_slide_trinkey_m0/). It ends in `.uf2`. Version 10.3.1 is the current stable release.
4. Copy the `.uf2` file onto TRINKEYBOOT. The board restarts, TRINKEYBOOT goes away, and a drive named CIRCUITPY appears.

## Install the firmware

1. Copy `code.py` and the `lib` folder from [firmware/slider-trinkey](../firmware/slider-trinkey/README.md) onto CIRCUITPY, replacing the files there.
2. Wait a few seconds. The board restarts on its own and starts sending readings.

## Connect the slider to the viewer

1. Plug the slider into a USB port.
2. Open the viewer in Chrome or Edge.
3. In the Main menu, select Settings.
4. Under Hardware Controls, check "Slider (Trinkey)".
5. Close Settings. A section headed "Trinkey Slider" now appears on the main page.
6. In the Trinkey Slider section, select Connect USB.
7. In the browser's port list, choose the Slider Trinkey.
8. Wait for the viewer to say "Trinkey Slider connected."

## Use it

- Slide the knob to change the depth. The viewer says the new depth once the knob has been still for about half a second.
- Changes smaller than 2 percent are ignored, so the depth does not drift while the knob is still.
- To stop, select Disconnect in the Trinkey Slider section, or unplug the board.

## Troubleshooting

**The viewer says the Web Serial API is not supported.** Use Chrome or Edge on a desktop computer.

**The slider is not in the port list.** Check that the cable or adapter carries data. Unplug the board and plug it in again. If no CIRCUITPY drive appears, install CircuitPython again.

**Connect USB fails with an error.** Another program may have the port open, such as the serial console in the Mu editor or a terminal. Close it, then select Connect USB again.

**The viewer connects but the depth never changes.** The board is not running this repository's firmware. Install the firmware again.

## Serial format

This section is for developers. The driver is `static/js/trinkey-slider.js` in [cad-a11y](https://github.com/cad-accessibility/cad-a11y).

- The viewer offers ports with USB vendor ID `0x239A` and product ID `0x8102` first, and falls back to every port if none match.
- The firmware prints one line per reading: `Slider: ` followed by a number from 0 to 100, then a newline.
- The viewer averages every 4 readings, clamps the result to 0 to 100, and rounds it. It updates the depth when the value moves by 2 or more, and announces it after 400 ms without a change.
- The port is a USB serial device, so the baud rate does not matter. The viewer opens it at 9600.
