from kb import KMKKeyboard
from kmk.keys import KC

# TODO: Check which modules you really need! The nice!nano has very limited storage and every line counts!
# Removing comments also helps save space!
#  from kmk.modules.<your module> import <Module>

keyboard = KMKKeyboard()

#  keyboard.modules.append(<Module>())

# if you want to debug your keymap, uncomment the following
#  keyboard.debug_enabled = True

# if you need space simply delete this comment and the debug toggle code below
#  def toggle_debug(*args, **kwargs):
#      keyboard.debug_enabled = not keyboard.debug_enabled
#  DB_TOGG = KC.NO.clone()
#  DB_TOGG.after_press_handler(toggle_debug)

# easier to write, but also takes space ;-)
#  xxx = KC.NO
#  ___ = KC.TRNS

# fun and useless led control (delete for more space and don't forget to remove
# mentions of INCLED and DECLED from your keymap!)
led_status = 0
n_led = 3
def _led(inc=True):
    global led_status
    led_status = (led_status + (2*inc - 1)) % (n_led + 1)
    status_array = [0 for i in range(n_led)]
    print(f'\n    global LED status: {led_status}')
    for led, status in enumerate(status_array):
        if led_status > led:
            status = 50
        else:
            status = 0
        print(f'    - status of led {led}: {status}')
        keyboard.led_ext.set_brightness(status, leds=[led])
def inc_led(*args, **kwargs):
    _led(inc=True)
def dec_led(*args, **kwargs):
    _led(inc=False)
INCLED = KC.NO.clone()
INCLED.after_press_handler(inc_led)
DECLED = KC.NO.clone()
DECLED.after_press_handler(dec_led)

# toggle leds on/off
TOGLED = KC.LED_TOG()

keyboard.keymap = [
    [
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,     KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,     KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,     KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
                                   KC.ESC,  KC.SPC,   KC.ENT,  KC.BSPC,
        # encoders: left cw, ccw,   right cw, ccw
                                   KC.RGHT, KC.LEFT, DECLED, INCLED,
    ],
]

if __name__ == '__main__':
    keyboard.go_ble()
