import gui
from tkinter import *

if __name__ == "__main__":
    root = Tk()

    ####Centers Window####
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('+%d+%d' % (x, y))  ## this part allows you to only change the location
    ########################

    my_gui = gui.MyFirstGUI(root)
    root.mainloop()