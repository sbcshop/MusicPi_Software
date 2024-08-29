''' Demo code to test onboard USER Buttons '''

import time
import board
from digitalio import DigitalInOut, Direction, Pull
from time import sleep

BT1 = DigitalInOut(board.GP2)
BT2 = DigitalInOut(board.GP3)
BT3 = DigitalInOut(board.GP4)

BT1.direction = Direction.INPUT
BT2.direction = Direction.INPUT
BT3.direction = Direction.INPUT


print("Press Any Button!")

while True:
    btn1 = BT1.value
    btn2 = BT2.value
    btn3 = BT3.value
    
    if btn1 == 0:
        print("BT1 Pressed!")
        sleep(0.2) # sleep for debounce
    
    if btn2 == 0:
        print("BT2 Pressed!")
        sleep(0.2)
    
    if btn3 == 0:
        print("BT3 Pressed!")
        sleep(0.2)
        
    sleep(0.2) # wait
