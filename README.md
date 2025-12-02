# Aryav's Macropad

MiPad is a 3x3 macropad that is made for KMK firmware.

## Features:
- Sleek squircle design
- 9 Kailh low-profile switches
- Two-tone

## CAD Model:
Everything fits in together by slotting into the parts. I plan to improve the mounting mechanism in the future (and will likely have to fine tune some things once I have the PCB), but for now it just uses slot mechanisms. 

There are 2 parts to the case: the top face and the bottom casing. I made it in Fusion360.  

<img src=assets/CAD.png alt="Schematic" width="500"/>

## PCB
I made the PCB in KiCad, and used KiBuzzard to make the fun text. 

Schematic
<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB
<img src=assets/pcb.png alt="Schematic" width="300"/>

I used Kailh's choc v2 key switch footprints, but used MX style spacing in this build. 

## Firmware Overview
This hackpad uses KMK firmware for everything. 

- the 6 keys are currently used for media controls for music, screen brightness changers, and a layer switch. 
- currently, I only have 1 layer implemented, but I'm going to be adding some more later on. 
- the OLED currently displays layer # and I plan to add some woodstock animations in the future.


## BOM:

- 9x Kailh Spring Mini Low-Profile Switches (I have these already, from another build)
- 9x Choc-v2 compatible Keycaps (I also have these already from another build)
- 1x PCB
- 1x XIAO RP2040
- 1x Case (2 printed parts)