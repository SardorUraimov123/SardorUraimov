from tkinter import *
from random import randint
import time
import threading

root = Tk()
root.attributes("-topmost", 0)
root.overrideredirect(1)
root.attributes("-alpha", 1)


def placewindows():
    while True:
        win = Toplevel(root)
        win.geometry("300x60+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(
            randint(0, root.winfo_screenwidth() - 64)))
        win.overrideredirect(1)
        Label(win, text="You hacked", fg="red").place(relx=.30, rely=.3)
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        time.sleep(.05)


threading.Thread(target=placewindows).start()

root.mainloop()