''' Demo code to test onboard RGB LED '''

import time
import board
import os
import neopixel

PIXEL_PIN = board.GP26  # pin that the RGB LED is connected to
ORDER = neopixel.RGB  # pixel color channel order

# RGBLED COLOR (GREEN, RED, BLUE)
RED = (0, 255, 0)
YELLOW = (255, 255, 0)
GREEN = (255, 0, 0)
CYAN = (255, 0, 255)
BLUE = (0, 0, 255)
PURPLE = (0, 255, 255)
CLEAR = (0, 0, 0) 

pixel = neopixel.NeoPixel(PIXEL_PIN, 1, pixel_order=ORDER, brightness=0.3)


while True:
    pixel[0] = RED
    time.sleep(2)
    pixel[0] = GREEN
    time.sleep(1)
    pixel[0] = CYAN
    time.sleep(1)
    pixel[0] = PURPLE
    time.sleep(1)
    pixel[0] = CLEAR
    time.sleep(1)
    
    

