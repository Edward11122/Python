from tkinter import *
from tkinter import filedialog
from pathlib import Path
import os


filename = "*.txt"

# Window config
root = Tk()
root.title(f"EDWARD NOTEPAD - {filename}") #Title
root.geometry("640x480")

def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select Text File",
                                          filetypes=(("Text File", "*.txt"), ("All File", "*.*")),
                                          initialdir="C:/Users/edwar/Python/edwardnotepad.py")
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf-8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())
    filename = Path(filename).stem
    root.title(f"EDWARD NOTEPAD - {filename}")

def browse_dest_path():
    filesave = filedialog.asksaveasfilename(title="Save",
                                          defaultextension='.txt',
                                          filetypes=(("Text File", "*.txt"), ("All File", "*.*")),
                                          initialdir="C:/Users/edwar/Python/edwardnotepad.py")
    if filesave == "":
        return
    return filesave

def save_file():
    global filename
    file_path = browse_dest_path()
    filename = Path(file_path).stem
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(txt.get("1.0", END))
    root.title(f"EDWARD NOTEPAD - {filename}")
     





# Menu
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)



# Scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Contents
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)
scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()