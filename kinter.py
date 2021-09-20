from Utils.blocks import Function
from Utils.tkinter_helpers import make_menu
import tkinter as tk
from PIL import Image,ImageTk
from Utils.tkinter_helpers import *
from Utils.functions import getExecutableFunctions,getVariableFunctions,getAllFunctions

app = tk.Tk()

app.title("Box Programming")
app.geometry("1080x720")
app.resizable(0, 0)


back = tk.Frame(master=app,bg='black')
back.pack(fill=tk.BOTH, expand=1)

executableFunctions = getExecutableFunctions()
variableFunctions = getVariableFunctions()
allFunctions = getAllFunctions()

my_canvas = tk.Canvas(back)
my_canvas.pack(fill=tk.BOTH,expand=1,padx=20,pady=30)

m = make_menu(app,executableFunctions)

def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

# Event Handlers
app.bind("<Button-3>", do_popup)
app.bind("<B1-Motion>", lambda event:movingMousePressed(event,my_canvas))
app.bind("<Motion>", lambda event:movingMouse(event,my_canvas))
app.bind("<ButtonRelease-1>", lambda event:endMoving(event,my_canvas))
app.bind("<Double-Button-1>", lambda event:doubleClickHandler(event,my_canvas))
app.bind("<Key>", lambda event:keyHandler(event,my_canvas))
app.bind("<Button-1>",clickHandler)

app.mainloop()