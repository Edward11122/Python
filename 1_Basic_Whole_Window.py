from PIL import Image       # to store image as files
import pyautogui as pag     # Screenshot
import time                 # Time for delay and filename etc...

time.sleep(3)       #delay 3 seconds

filepath = 'C:/Users/edwar/Vision Coding/Screenshot/images'

for i in range(1, 11):                                      # Loop 1 to 10      range(first, last-1)
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")
    time.sleep(2)                                           # take with delay 2 seconds





