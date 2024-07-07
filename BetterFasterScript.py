import pydirectinput as p
import time
import pyautogui as pt
import keyboard

# import cv2
# import numpy as np
# import threading as th


# ------------------------------------------------------------------------------------------------ #


#  This is a script for Minecraft Java to make a mining bot with minimal inteligence
#  X basic movement for 2x2 tunnel
#  X image recognition
#  V reaction to image
#  X lava reaction
#  - way to get it to continue mining after hitting lava
#  - ore reaction
#  - return to position aafter mining ore


# ------------------------------------------------------------------------------------------------ #


# helper function
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.7)

    if position is None:
        print(f"{image} not found...")
        return 0
    else:
        pt.moveTo(position, duration=0.1)
        pt.moveRel(off_x, off_y, duration=0.1)
        pt.click(clicks=clicks, interval=0.3)


# main functions


# mines block
def mineblock():
    p.mouseDown()
    time.sleep(0.3)
    p.mouseUp()


# walks forward
def walkf():
    p.keyDown("shift")
    p.keyDown("w")
    time.sleep(0.7)
    p.keyUp("w")
    p.keyUp("shift")
    time.sleep(0.5)


# walk backwards
def walkb():
    p.keyDown("s")
    time.sleep(1.5)
    p.keyUp("s")
    time.sleep(0.5)


# walk right
def walkr():
    p.keyDown("d")
    time.sleep(0.13)
    p.keyUp("d")


# walk left
def walkl():
    p.keyDown("a")
    time.sleep(0.13)
    p.keyUp("a")


# lava recognition
def locate_lava():
    position = pt.locateCenterOnScreen("images/lava_id.png", confidence=0.8)

    if position is None:
        return False
    else:
        # Move backwards to avoid burning
        walkb()
        print("Found lava")
        return True


# stop switch system
def switch(keyboard_event_info):
    global stop_switch

    stop_switch = True

    keyboard.unhook_all()
    print(keyboard_event_info)


# ----------------------------------------------------------------------------------------------------------------- #

# Plan for ore recognition

# using threading to work simultaneously with standard mining script
# use screen space to look for a colour outside of the monochrome palette
# once found obtain location of discovered pixel
# once found subtract the number from the origin at the crosshair
# use that number to move the cursor to the block
# break block
# loop


# main script


# variables
counter = 0

stop_switch = False


# Resume Game
p.click(960, 324)
# p.click(1426, 411)
time.sleep(1)


# wakes up mouse movement
p.moveRel(0, 1)


# start of program
def main_function():
    global stop_switch

    keyboard.on_press_key("p", switch)

    while stop_switch is False:

        if stop_switch is False:
            if not locate_lava():
                mineblock()
            else:
                break

        if stop_switch is False:
            if not locate_lava():
                p.moveRel(0, 300)
                mineblock()
            else:
                break

        if stop_switch is False:
            if not locate_lava():
                p.moveRel(0, -300)
                walkr()
            else:
                break

        if stop_switch is False:
            if not locate_lava():
                mineblock()
            else:
                break

        if stop_switch is False:
            if not locate_lava():
                p.moveRel(0, 300)
                mineblock()
            else:
                break

        if stop_switch is False:
            if not locate_lava():
                p.moveRel(0, -300)
                walkl()
            else:
                break

        if stop_switch is False:
            if not locate_lava():
                walkf()
            else:
                break

    stop_switch = False


main_function()
