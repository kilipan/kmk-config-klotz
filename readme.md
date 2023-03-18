<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/GEIGEIGEIST/zmk-config-klotz/master/docs/images/KLOTZ_font_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/GEIGEIGEIST/zmk-config-klotz/master/docs/images/KLOTZ_font_bright.svg">
  <img alt="KLOTZ logo font" src="https://raw.githubusercontent.com/GEIGEIGEIST/zmk-config-klotz/master/docs/images/KLOTZ_font_bright.svg">
</picture>

# KMK CONFIG FOR THE KLOTZ SPLIT KEYBOARD

[Here](https://github.com/GEIGEIGEIST/klotz) you can find the hardware files and build guide for the KLOTZ.

KLOTZ is a 34 key column-staggered split keyboard running [KMK](https://github.com/KMKfw/kmk_firmware/) or [ZMK](https://zmk.dev/). It supports a low profile encoder and three status LEDs on every side.
You can find the ZMK firmware [here](https://github.com/GEIGEIGEIST/zmk-config-klotz).

![KLOTZ layout](https://raw.githubusercontent.com/GEIGEIGEIST/zmk-config-klotz/master/docs/images/KLOTZ_layout.svg)


## HOW TO USE

### Prerequisites
These are some things we need to get in order before flashing anything:
- Download the newest stable CircuitPython for the [nice!nano](https://circuitpython.org/board/nice_nano/), make note of the version! (8.0.4 at the time of writing)
- If your CircuitPython version is not 7.x or 8.x, you'll need to replace the `adafruit_ble` library with the [appropriate version](https://circuitpython.org/libraries).
- If you want to use the newest KMK version, be aware that you will have to [compile it!](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Officially_Supported_Microcontrollers.md#pre-compiling-kmk-for-nicenano) If anything breaks, note the date of the last commit in *this* repository (the one you are reading the readme of right now) and check for breaking changes in KMK that may have been introduced since then!

### Installation
You'll need to complete the following procedure for *both halves* of the KLOTZ split keyboard, with *almost* the same files (differences marked by **bold** text):
- First, enter the bootloader of the nice!nano.
- Flash your previously downloaded CircuitPython `.uf2` file.
- You should now see a USB drive labelled `CIRCUITPYTHON`.
- If there is a `code.py` file on that USB drive, *delete it!*
- Copy the entire *compiled* `kmk` directory from *this repo* or the KMK repository you cloned *and compiled* before and paste it onto the USB drive.
- Copy the entire `adafruit_ble` directory either from *this* repository or the one you downloaded before and paste it onto the drive.
- Copy the `kb.py` and `main.py` files from *this* repository onto the drive.
- If you are flashing the **LEFT** side of the KLOTZ, copy the file `rename_KLOTZ_left/boot.py` onto the drive.
- If you are flashing the **RIGHT** side of the KLOTZ, copy the file `rename_KLOTZ_right/boot.py` onto the drive.
- Reset the microcontroller. The USB drive should now be renamed to `KLOTZ_L` or `KLOTZ_R` (depending upon which side you are working on).
- That should be all! :)

### Setting up your personal keymap
The default keymap in this repo is just an example. Head over to the [KMK docs](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md) for details on how to personalize your KLOTZ!
