# The orientation cube

The orientation cube is a hand-sized 3D-printed cube with a WitMotion WT901BLECL motion sensor inside. Turn the cube so a different face points up, and the CAD A11y viewer switches to that face's standard view and says its name, for example "x+ view".

This page is about the current cube, built around the WitMotion sensor. The earlier cube, which held a GoDice die, is described in [gen1-viewcube.md](gen1-viewcube.md).

## Status

- **Parts** are listed in [bom/cube.csv](../bom/cube.csv).
- **Version v0.1.0 of the design** is in [hardware/cube](../hardware/cube/onshape.toml) as STEP and Parasolid files, for CAD programs. **Print files** are attached to each [release](https://github.com/cad-accessibility/tangible-controls/releases): one STL file per half, in millimeters, and a 3MF file with both halves.
- **Print settings** are below, from the slicer project used to print the cubes in use.

## What you need

- The parts in [bom/cube.csv](../bom/cube.csv).
- A 3D printer that can print 0.06 mm layers. The braille and the press fits need fine detail, so the print takes a long time.
- A computer with Chrome or Edge on Windows, macOS or ChromeOS. The viewer talks to the sensor over Web Bluetooth, which Firefox and Safari do not support.
- On macOS, Bluetooth permission for the browser. It is in System Settings, under Privacy and Security, then Bluetooth.

## The faces

The cube is about 62 mm across. It prints as two halves that press together: a taller upper half with a plain, closed top, and a shorter lower half that holds the sensor.

Each side face has its own texture and a braille label inside an oval outline. The label names the view the face stands for. The plus and minus signs follow the [UEB math convention](https://uebmath.aphtech.org/lesson1.3): dot 5 followed by dots 2-3-5 for plus, and dot 5 followed by dots 3-6 for minus.

| Face | Texture | Braille label |
| --- | --- | --- |
| x+ | Raised hexagons in rows | x, then the plus sign |
| x- | Raised hexagons in rows | x, then the minus sign |
| y+ | Wavy vertical ridges | y, then the plus sign |
| y- | Wavy vertical ridges | y, then the minus sign |
| Top and bottom | Plain | Not documented yet |

The textures run across the joint between the halves. A small half-round hole at the bottom of the edge where the x- and y- faces meet gives access to the sensor's power switch.

## Print the halves

These are the settings in the Bambu Studio project Felix Hähnlein used to print the cubes in use, on a Bambu Lab X1 Carbon:

- PLA, with both halves in one color.
- Layer height 0.06 mm, and 0.1 mm for the first layer.
- 4 walls, 7 top layers and 5 bottom layers.
- Infill 15%, grid pattern.
- No supports. Brim set to automatic.
- Seam position aligned.
- Elephant foot compensation 0.15 mm.
- Textured PEI plate.
- The upper half lies upside down, with its plain top face on the plate. The lower half lies on its base, with the pocket facing up.

The project is set up for a 0.2 mm nozzle, but Felix says the printer settings in it differ from the printer the cubes were printed on, so the nozzle size is unconfirmed. The settings above do not depend on the printer.

Fine layers are what make the braille and the press fits come out right, so expect a long print.

## Charge the sensor

1. Connect the sensor to a USB charger with its cable.
2. Leave it to charge.

WitMotion documents only light signals for the sensor, so a sighted helper may need to check them:

- A red light stays on while the battery charges and goes out when it is full.
- A blue light flashes quickly while the sensor waits for a connection, and slowly once it is connected.

## Put the cube together

Charge the sensor first.

1. Find the lower half: the shorter piece, with an open pocket inside and a small half-round hole at the bottom of one corner.
2. Hold the sensor with its printed label facing up.
3. Turn the sensor so its power switch faces the half-round hole.
4. Lower the sensor into the pocket, so its two mounting tabs sit at the ends of the pocket and it lies flat.
5. Feel through the hole for the power switch. If you can't reach it, lift the sensor out, turn it around and put it back.
6. Place the upper half on top, plain face up, with hexagons over hexagons and ridges over ridges.
7. Press the halves together until they meet all the way around. Four small press fits, half-sphere bumps at the joint, hold them closed.

## Connect the cube to the viewer

1. Open the viewer in Chrome or Edge.
2. In the Main menu, select Settings.
3. Under Hardware Controls, check "Cube (WitMotion IMU)".
4. Close Settings. A section headed "WitMotion IMU" now appears on the main page.
5. Put the cube on the table with its plain top face up, the closed end of the taller half. Leave it still. The next section explains why.
6. In the WitMotion IMU section, select Connect BLE.
7. In the browser's device list, choose the device whose name starts with WT.
8. Wait for the viewer to say "WitMotion IMU connected."

If the device list is empty, see [Troubleshooting](#troubleshooting).

## The reference position

The viewer measures the cube's tilt from a reference position. The reference is the cube's position in the first reading the viewer receives at least 20 seconds after the page opened. That position counts as level, with z+ on top.

- Keep the cube still, plain top face up, until the page has been open for 20 seconds and you have connected.
- Disconnecting and connecting again does not reset the reference. To set it again, reload the page and connect again.
- If the views stop matching the faces, put the cube flat on the table, reload the page and connect again.

## Use it

- Turn the cube so another face points up. When a different face is on top, the viewer switches to that view and says its name.
- Tipping the cube onto one of its four sides gives x+, x-, y+ or y-. Turning it upside down gives z-.
- Spinning the cube on the table, like turning a dial, never changes the view. Only the face on top matters.
- The view stays the same while the same face is closest to up, so you can hold the cube at an angle.
- To check the cube, tip it so the face labeled x+ points up. The viewer should say "x+ view". If it names another view, put the cube plain top face up, reload the page and connect again.

## Troubleshooting

**The viewer says the Web Bluetooth API is not supported.** Use Chrome or Edge on Windows, macOS or ChromeOS.

**The device list is empty.** The sensor may be off, out of charge, out of range, or already connected to another tab or app. Charge it, move it closer, close other tabs that use it, then select Connect BLE again.

**The viewer says "WitMotion IMU disconnected." right after you choose the device.** The device you chose is not a supported WitMotion sensor. The status line under Connect BLE says "No supported service found on device." Choose the device whose name starts with WT.

**After reloading the page, the cube does nothing.** The browser does not reconnect on its own. Select Connect BLE again.

**The view keeps switching between two faces.** The cube is close to halfway between them. Tilt it further toward the face you want.

**The view jumps to z+ for a moment.** A damaged or partial reading from the sensor can be read as level. Keep turning the cube; the next good reading corrects it.

## Known issues

These come from the driver in cad-a11y and will be fixed when the driver moves to this repository.

- The reference is taken 20 seconds after the page loads, not when you connect, and only a page reload resets it.
- There is no tolerance near the halfway point between two faces, so the view can switch back and forth, with an announcement each time.
- A partial reading can jump the view to z+.
- When the device is not supported, the viewer announces "disconnected" instead of the real problem.

## How the view is chosen

This section is for developers. The driver is `static/js/witmotion-imu.js` in [cad-a11y](https://github.com/cad-accessibility/cad-a11y).

1. The sensor sends its angles over Bluetooth Low Energy, by default 10 times a second. The driver subscribes to characteristic `0000ffe4` of service `0000ffe5`, and falls back to `0000ffe1` of service `0000ffe0`.
2. Two frame types carry angles. `55 61` is 20 bytes: acceleration, angular velocity, then roll, pitch and yaw, with no checksum. `55 53` is 11 bytes: roll, pitch, yaw and temperature, then a checksum. Each angle is a signed 16-bit little-endian value; degrees = value / 32768 × 180.
3. The driver subtracts the reference angles from each reading.
4. It builds a rotation matrix R = Rz(yaw) · Ry(pitch) · Rx(roll), rotates each face's normal by R, and picks the face whose rotated normal points most nearly up.

Yaw is a rotation about the vertical axis, which never changes how far a vector points up. So yaw never affects the result, and the sensor's magnetometer needs no calibration.

Face normals, in the sensor's frame:

| View | Normal (x, y, z) |
| --- | --- |
| x+ | (0, -1, 0) |
| x- | (0, 1, 0) |
| y+ | (1, 0, 0) |
| y- | (-1, 0, 0) |
| z+ | (0, 0, 1) |
| z- | (0, 0, -1) |

The view for each turn away from the reference:

| Turn from the reference | View |
| --- | --- |
| None | z+ |
| Roll +90 degrees | x- |
| Roll -90 degrees | x+ |
| Pitch +90 degrees | y- |
| Pitch -90 degrees | y+ |
| Roll 180 degrees | z- |
