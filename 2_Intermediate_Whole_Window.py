from PIL import Image       # to store image as files
import pyautogui as pag     # Screenshot
import time                 # Time for delay and filename etc...
import keyboard             # To check pressed keyboard  

filepath = 'C:/Users/edwar/Vision Coding/Screenshot/images'

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")

while True:
    if keyboard.is_pressed("ctrl + 9"):    # recognize while button is pressed
        screenshot()
    elif keyboard.is_pressed("esc"):
        break