from storage import getmount
from kmk.hid import HIDModes
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.nice_nano import pinout as pins
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.extensions.LED import LED


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins=self.col_pins,
                row_pins=self.row_pins,
                # optional arguments with defaults:
                columns_to_anodes=self.diode_orientation,
                interval=0.02, # Debounce time in floating point seconds
                max_events=64,
            ),
            RotaryioEncoder(
                pin_a=self.encoder_a,
                pin_b=self.encoder_b,
                divisor=4,
            ),
        ]
        self.modules.append(Split(split_side=self.side, split_target_left=True, split_type=SplitType.BLE))
        self.extensions.append(self.led_ext)

    def go_ble(self, *args, **kwargs):
        if self.side == SplitSide.LEFT:
            self.go(*args, hid_type=HIDModes.BLE, **kwargs)
        else:
            self.go(*args, **kwargs)

    side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

    row_pins = (pins[8], pins[9], pins[10], pins[11])
    col_pins = (pins[16], pins[15], pins[14], pins[13], pins[12])
    diode_orientation = DiodeOrientation.COL2ROW

    encoder_a = pins[18]
    encoder_b = pins[17]

    led_pins = [pins[5], pins[6], pins[7]]
    led_ext = LED(led_pin=led_pins)
    
    coord_mapping = [
      0,  1,  2,  3,  4,   26, 25, 24, 23, 22,
      5,  6,  7,  8,  9,   31, 30, 29, 28, 27,
     10, 11, 12, 13, 14,   36, 35, 34, 33, 32,
                 18, 19,   41, 40,
                 20, 21,   42, 43,
    ]
