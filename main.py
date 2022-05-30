import time
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key
from PIL import ImageGrab

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

RACES_NEEDED = 4  # Default 500 for achievement

# Button Locations and colors
RACE_MENU_BUTTON = (2450, 690)
RACE_MENU_BUTTON_COLOR = (218, 149, 60)

RACE_BUTTON = (1120, 1140)
RACE_BUTTON_COLOR = (26, 85, 15)

RACE_EVENT_POPUP = (677, 933)
RACE_EVENT_POPUP_COLOR = (87, 141, 212)

HOME_BUTTON = (1280, 1120)
HOME_BUTTON_COLOR = (255, 255, 255)


def wait_for(pixel: tuple[int, int], color: tuple[int, int, int]):
    """Wait until conditions are met for color at a specific pixel."""
    while True:
        if get_pixel_color(pixel) == color:
            return


def get_pixel_color(pixel: tuple[int, int]):
    image = ImageGrab.grab()
    return image.getpixel(pixel)


def run_race():
    """
    Run from the main home screen of Bloons TD6 and already have race pass active.
    Function should return to home screen to reloop
    """
    wait_for(RACE_MENU_BUTTON, RACE_MENU_BUTTON_COLOR)

    mouse.position = RACE_MENU_BUTTON
    mouse.click(Button.left)

    wait_for(RACE_BUTTON, RACE_BUTTON_COLOR)

    mouse.position = RACE_BUTTON
    mouse.click(Button.left)

    wait_for(RACE_EVENT_POPUP, RACE_EVENT_POPUP_COLOR)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    time.sleep(1)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

    wait_for(HOME_BUTTON, HOME_BUTTON_COLOR)

    mouse.position = HOME_BUTTON
    mouse.click(Button.left)


if __name__ == "__main__":
    for _ in range(RACES_NEEDED):
        run_race()
