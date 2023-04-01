import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image       # to store image as files
import pyautogui as pag     # Screenshot
import time                 # Time for delay and filename etc...
import keyboard             # To check pressed keyboard  
from io import BytesIO
import win32clipboard
from datetime import datetime

root = Tk()
root.title("Edward_Screenshot")
root.geometry("480x180+300+300")

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








# Save Path Function
def browse_dest_path():
    global filepath 
    filepath = filedialog.askdirectory(initialdir='C:/Users/edwar/Vision Coding/Screenshot/images')
    if filepath == "":
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0, filepath)

# Start Function
def start():
    # Get Each Options
    global stop
    stop = False
    # Check Save Path
    if len(txt_dest_path.get()):
        msgbox.showwarning("Warning", "Select save path")
        return
    
    global select_var
    if select_var.get() == 1:
        Clipboard_Screenshot()
    elif select_var.get() == 2:
        Imagefile_Screenshot()
    else: 
        msgbox.showwarning("ERROR", "Select SCR MODE")
        return

# File Frame
select_frame = Frame(root)
select_frame.pack(fill = "x", padx=5, pady=5)

# Select Mode
select_var = IntVar()
btn_mode1 = Radiobutton(select_frame, text="Clipboard", value=1, variable=select_var).pack(side='left')
btn_mode2 = Radiobutton(select_frame, text="ImageFile", value=2, variable=select_var).pack(side='right')

# Save path Frame
path_frame = LabelFrame(root, text="save Path")
path_frame.pack(fill = "x", padx=5, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.insert(0, filepath)
txt_dest_path.pack(side="left",fill="x", expand=True, padx=5, pady=5)

btn_dest_path = Button(path_frame, text="browse..", width=18, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# Execute Frame
frame_run = Frame(root)
frame_run.pack(fill = "x", padx=5, pady=5)

btn_close = Button(frame_run, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="left", padx=5, pady=5)

btn_start = Button(frame_run, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False,False)
root.mainloop()