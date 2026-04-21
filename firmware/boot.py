"""
Boot configuration for Macropad
Seeed Studio Xiao RP2040 with KMK firmware

This file runs before main.py and sets up I2C for the OLED display.
"""

import board
import busio

# Initialize I2C for OLED display
# SDA = GP6, SCL = GP7
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)

