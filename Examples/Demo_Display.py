''' Demo Code for onboard 1.14" TFT Display '''

import time
import digitalio
import board
import busio
import terminalio
import displayio
from digitalio import DigitalInOut, Direction
from time import sleep
from adafruit_st7789 import ST7789
from adafruit_display_text import label

BT1 = DigitalInOut(board.GP2)
BT2 = DigitalInOut(board.GP3)
BT3 = DigitalInOut(board.GP4)

BT1.direction = Direction.INPUT
BT2.direction = Direction.INPUT
BT3.direction = Direction.INPUT

# Declare some parameters used to adjust style of text and graphics
BORDER = 5
FONTSCALE = 2
FONTSCALE1 = 3

# some predefine colors
WHITE = 0xFFFFFF  
RED = 0xff0000    
YELLOW = 0xFFFF00 
BLUE = 0x00000FF
GREEN = 0x00FF00
PURPLE = 0xFF00FF
BLACK = 0x000000

# Release any resources currently in use for the displays
displayio.release_displays()

tft_clk = board.GP14 # must be a SPI CLK
tft_mosi= board.GP15 # must be a SPI TX
tft_rst = board.GP12
tft_dc  = board.GP6
tft_cs  = board.GP13
tft_bl  = board.GP7 #GPIO pin to control backlight LED
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)

#define led (as backlight) pin as output
BackLightLED = digitalio.DigitalInOut(tft_bl)
BackLightLED.direction = digitalio.Direction.OUTPUT
BackLightLED.value=True

# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7789(display_bus, rotation=90, width=240, height=135, rowstart=40, colstart=53)

# Make the display context
splash = displayio.Group()
display.show(splash)


def display_clear():
    color_bitmap = displayio.Bitmap(display.width, display.height, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = BLACK

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)


#Function to print data on TFT
def print_onTFT(text, x_pos, y_pos, font_scale=FONTSCALE, txt_color = WHITE): 
    text_area = label.Label(terminalio.FONT, text=text, color=txt_color)
    text_group = displayio.Group(scale=font_scale,x=x_pos,y=y_pos)
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)

print_onTFT("Hello...!", 20, 20, 2, WHITE )  # Pass text, x, y, fontsize, hex_color
time.sleep(1)

display_clear()
print_onTFT("MusicPi", 30, 60, 4, YELLOW)
time.sleep(3)
 
display_clear() 
print_onTFT("Thank You", 40, 30, 3, YELLOW)
print_onTFT("SB COMPONENTS", 20, 80, 2, BLUE)
print_onTFT("https://shop.sb-components.co.uk/", 20, 100, 1, WHITE)
time.sleep(1)

print("Press Any Button!")

while True:
    btn1 = BT1.value
    btn2 = BT2.value
    btn3 = BT3.value
    
    if btn1 == 0:
        display_clear() 
        print_onTFT("BT1 Pressed!", 30, 30, 2, RED)
        print("BT1 Pressed!")
        sleep(1)
    
    if btn2 == 0:
        display_clear() 
        print_onTFT("BT2 Pressed!", 30, 30, 2, YELLOW)
        print("BT2 Pressed!")
        sleep(0.2)
    
    if btn3 == 0:
        display_clear() 
        print_onTFT("BT3 Pressed!", 30, 30, 2, PURPLE)
        print("BT3 Pressed!")
        sleep(0.2)
        
    sleep(0.2) # wait


