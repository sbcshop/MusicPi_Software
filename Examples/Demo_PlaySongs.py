''' Demo to play songs stored in SDcard
    Usage:
    create .mp3 song files as per instructions available on Github:
    
'''

import time, array, math, os, storage
import audiocore, audiobusio, audiomixer, audiomp3, audiobusio
import board, busio, displayio, terminalio
import adafruit_sdcard
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from time import sleep
from adafruit_st7789 import ST7789
from adafruit_display_text import label
import sys

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

PIXEL_PIN = board.GP26  # pin that the RGB LED is connected to
ORDER = neopixel.RGB  # pixel color channel order

pixel = neopixel.NeoPixel(PIXEL_PIN, 1, pixel_order=ORDER, brightness=0.3)

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
BackLightLED = DigitalInOut(tft_bl)
BackLightLED.direction = Direction.OUTPUT
BackLightLED.value=True

# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7789(display_bus, rotation=90, width=240, height=135, rowstart=40, colstart=53)

# Make the display context
splash = displayio.Group()
display.show(splash)

#define and configure I2S pin 
audio = audiobusio.I2SOut(board.GP10, board.GP11, board.GP9)

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
    
def play_song():
    try:
        btn3 = BT3.value
        mp3_files = sorted("/sd/songs/" + fn for fn in os.listdir("/sd/songs/") if fn.lower().endswith("mp3"))
        print(mp3_files)
        
        if len(mp3_files) == 0:
            pixel[0] = (0, 255, 0)
            time.sleep(0.5)
            pixel[0] = (0, 0, 0)
            time.sleep(0.5)
            print("N0, MP3  Files")
            display_clear() 
            print_onTFT("N0, MP3  Files", 5, 30, 2, PURPLE)
            return
        
        for filename in mp3_files:
            decoder = audiomp3.MP3Decoder(filename)
            decoder.file = open(filename, "rb")
            audio.play(decoder)
            
            file_playname = filename.split('/')
            print(file_playname[3])
            print("Playing:", filename)
            
            display_clear() 
            print_onTFT("Playing..", 5, 30, 2, PURPLE)
            print_onTFT(file_playname[3], 5, 60, 2, YELLOW)
            pl = 0
            while audio.playing:
                btn2 = BT2.value
                
                if btn2 == 0:
                    print("Play Next Song!")
                    audio.stop()
        
                time.sleep(0.1)
                
        print("Done!")
        sel_choice()
        
    except OSError as e:
        audio.stop()
        print("Error:", e)
        return

    except KeyboardInterrupt as k:
        audio.stop()
        print("Error:", e)
        return
    
def sel_choice():
    display_clear() 
    print_onTFT("BT1 - Play", 40, 30, 2, GREEN)
    print_onTFT("BT2 - Next", 40, 60, 2, YELLOW)
    time.sleep(1)
    pixel[0] = (0, 0, 0)

    print("Press Any Button!")
    
SD_spi = busio.SPI(board.GP18, board.GP19, board.GP16)   # SDcard SPI(CARD_CLK, CARD_MOSI, CARD_MISO)
SD_cs = DigitalInOut(board.GP17)  #chip select 
num_voices = 1

print_onTFT("Hello...!", 20, 20, 2, WHITE )  # Pass text, x, y, fontsize, hex_color
time.sleep(1)

display_clear()
print_onTFT("MusicPi", 30, 60, 4, YELLOW)
time.sleep(2)

try:
    sdcard = adafruit_sdcard.SDCard(SD_spi, SD_cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    pixel[0] = (255, 0, 0)  # GREEN COLOR for RGBLed
    time.sleep(1)
    sel_choice()
    
except OSError as e:
    pixel[0] = (0, 255, 0)  # RED COLOR for RGBLed
    display_clear()
    print_onTFT("Please Insert", 10, 20, 2, YELLOW)
    print_onTFT("SDcard", 10, 60, 2, YELLOW)
    print("Error:", e)
    
    
while True:
    btn1 = BT1.value
    
    if btn1 == 0:
        sleep(0.5)
        pixel[0] = (0, 255, 0)  # RED COLOR for RGBLed 
        play_song()
    
    sleep(0.2) # wait



