"""
Grabs the mouse cursor position and gets the color of that pixel 1 second after. Mouse should be moved
in this 1 second window to avoid the cursor color being recorded
Ctrl + C to End
"""
import time
from main import mouse, get_pixel_color

if __name__ == "__main__":

    while True:
        position = mouse.position
        print(f"POSITION: {position}")
        time.sleep(1)
        print(f"COLOR: {get_pixel_color(position)}")
        time.sleep(1)
        print()
