from PIL import Image       # to store image as files
import pyautogui as pag     # Screenshot
import time                 # Time for delay and filename etc...
import keyboard             # To check pressed keyboard  
from io import BytesIO
import win32clipboard
from datetime import datetime


filepath = 'C:/Users/edwar/Vision Coding/Screenshot/images'


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def Clipboard_Screenshot():
    while True:
        go_on = True

        if keyboard.is_pressed("ctrl + 9"):
            while True:
                start_time = datetime.now()
                start = pag.position()          # To input mouse's position in 'start' variable // x point = start[0], y = start[1]
                time.sleep(0.2)
                break

            while True:
                now_time = datetime.now()
                if (now_time - start_time).total_seconds() > 5:
                    go_on = False
                    break
                if keyboard.is_pressed("ctrl + 9"):
                    end = pag.position()        # To input mouses position in 'End' varibale // x point = end[0], y = end[1]
                    time.sleep(0.2)
                    break

            if go_on:

                # X point
                if start[0] == end[0]:
                    go_on = False
                    continue
                elif start[0] < end[0]:
                    x_point = start[0]
                else:
                    x_point = end[0]

                # Y point
                if start[1] == end[1]:
                    go_on = False
                    continue
                elif start[1] < end[1]:
                    y_point = start[1]
                else:
                    y_point = end[1]

                # Width / Height
                width = abs(end[0]-start[0])
                height = abs(end[1]-start[1])

                tempimage = f"{filepath}/temp.png"
                pag.screenshot(tempimage, region = (x_point, y_point, width, height))
                image = Image.open(tempimage)

                output = BytesIO()
                image.convert('RGB').save(output, 'BMP')
                data = output.getvalue()[14:]
                output.close()

                send_to_clipboard(win32clipboard.CF_DIB, data)

        elif keyboard.is_pressed("esc"):
            break

def Imagefile_Screenshot():
    range = False
    while True:
        go_on = True

        if keyboard.is_pressed("ctrl + 9"):
            while True:
                range = True
                start_time = datetime.now()
                start = pag.position()          # To input mouse's position in 'start' variable // x point = start[0], y = start[1]
                time.sleep(0.2)
                break

            while True:
                now_time = datetime.now()
                if (now_time - start_time).total_seconds() > 5:
                    go_on = False
                    break
                if keyboard.is_pressed("ctrl + 9"):
                    end = pag.position()        # To input mouses position in 'End' varibale // x point = end[0], y = end[1]
                    time.sleep(0.2)
                    break

            if go_on:

                # X point
                if start[0] == end[0]:
                    go_on = False
                    continue
                elif start[0] < end[0]:
                    x_point = start[0]
                else:
                    x_point = end[0]

                # Y point
                if start[1] == end[1]:
                    go_on = False
                    continue
                elif start[1] < end[1]:
                    y_point = start[1]
                else:
                    y_point = end[1]

                # Width / Height
                width = abs(end[0]-start[0])
                height = abs(end[1]-start[1])

        elif keyboard.is_pressed('shift'):
            curr_time = time.strftime("_%Y%m%d_%H%M%S")
            if range:
                pag.screenshot(f"{filepath}/image{curr_time}.png", region=(x_point, y_point, width, height))
                range = False
            else:
                pag.screenshot(f"{filepath}/image{curr_time}.png")
        elif keyboard.is_pressed("esc"):
            break

mode = 'temp'
while mode != 'exit':
    print('hi')
    mode = input(' [1] Clipboard \n [2] Imagefile \n [exit] Program Quit \n >>>')
    if mode == '1':
        Clipboard_Screenshot()
    elif mode == '2':
        Imagefile_Screenshot()
    elif (mode == 'exit') or (keyboard.is_pressed('esc')):
        break
    else :
        print('Error input 1 or 2 or exit')