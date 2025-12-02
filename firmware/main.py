"""
KMK Firmware for Custom 6-Key Macropad
Hardware: Seeed Studio Xiao RP2040
- 6 direct-wired switches
- 2 SK6812 mini LEDs on GP26
- SSD1306 OLED (128x32 or 128x64) on I2C (GP6/GP7)
"""

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DigiKeyScanner
from kmk.extensions.RGB import RGB
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType
from kmk.modules.layers import Layers

# Initialize the keyboard
keyboard = KMKKeyboard()

# Define the 6 direct-wired switch pins
keyboard.matrix = DigiKeyScanner(
    pins=(
        board.GP1,
        board.GP2,
        board.GP4,
        board.GP3,
        board.GP27,
        board.GP28,
    )
)

# Configure RGB LEDs (SK6812 mini)
rgb = RGB(
    pixel_pin=board.GP26,
    num_pixels=2,
    val_limit=100,  # Brightness limit (0-255)
    val_default=50,  # Default brightness
    animation_mode='static',  #static, breathing, rainbow, etc.
)
keyboard.extensions.append(rgb)

# Configure OLED display
oled = Oled(
    OledData={
        'display_type': 'SSD1306',  # Display type
        'i2c': board.I2C,  # Uses I2C initialized in boot.py
        'device_address': 0x3C,  # I2C address
        'width': 128,  # Display width in pixels
        'height': 32,  # Display height (use 64 if you have 128x64 display)
    },
    toDisplay={
        OledReactionType.STATIC: [
            {
                OledDisplayMode.TXT: ['Macropad', 'Ready!', 'Layer: 0'],
            }
        ],
        OledReactionType.LAYER: [
            {
                OledDisplayMode.TXT: ['Layer 0', 'Media + Bright'],
            },
            {
                OledDisplayMode.TXT: ['Layer 1', 'Custom Macros'],
            }
        ],
    },
    flip=False,  #True if display is upside down
)
keyboard.extensions.append(oled)

# Enable layers module
layers = Layers()
keyboard.modules.append(layers)

# Layer 0: Media controls + brightness + layer switch
# Layer 1: for future video editing/MIDI functions
keyboard.keymap = [
    # Layer 0 (default)
    [
        KC.MPRV,   # Key 1 (GP1) - Previous track
        KC.MPLY,   # Key 2 (GP2) - Play/Pause
        KC.MNXT,   # Key 3 (GP4) - Next track
        KC.BRIU,   # Key 4 (GP3) - Brightness up
        KC.BRID,   # Key 5 (GP27) - Brightness down
        KC.MO(1),  # Key 6 (GP28) - Hold for layer 1
    ],
    # Layer 1 (hold key 6 to access)
    [
        KC.F13,    # Key 1 - Placeholder for future macros
        KC.F14,    # Key 2 - Placeholder for future macros
        KC.F15,    # Key 3 - Placeholder for future macros
        KC.F16,    # Key 4 - Placeholder for future macros
        KC.F17,    # Key 5 - Placeholder for future macros
        KC.TRNS,   # Key 6 - Transparent (still acts as layer switch)
    ]
]

if __name__ == '__main__':
    keyboard.go()
