from Utils.blocks import Function
from Utils.tkinter_helpers import make_menu
import tkinter as tk
from Utils.tkinter_helpers import *
from Utils.helpers import getExecutableFunctions,getVariableFunctions,getAllFunctions,_from_rgb
from PIL import Image,ImageTk
from Utils.global_vars import ALL_GLOBALS

app = tk.Tk()

app.title("Box Programming")
app.geometry("1080x720")
app.resizable(0, 0)

ALL_GLOBALS["app"] = app

back = tk.Frame(master=app,bg='black')
back.pack(fill=tk.BOTH, expand=1)

executableFunctions = getExecutableFunctions()
variableFunctions = getVariableFunctions()
allFunctions = getAllFunctions()

my_canvas = tk.Canvas(back,bg=_from_rgb((33,33,33)))
my_canvas.pack(fill=tk.BOTH,expand=1,padx=20,pady=30)

ALL_GLOBALS["canvas"] = my_canvas

m = make_menu(app,allFunctions)

init_builtins()

def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

pilImage = Image.open("imgs/ok/empty (2).png")
pilImage = pilImage.resize((50,30))
image = ImageTk.PhotoImage(pilImage)
app.empty_execute_image = image
pilImage = Image.open("imgs/ok/full (2).png")
pilImage = pilImage.resize((50,30))
image = ImageTk.PhotoImage(pilImage)
app.full_execute_image = image

# Event Handlers
app.bind("<Button-3>", do_popup)
app.bind("<B1-Motion>", lambda event:movingMousePressed(event,my_canvas,app))
app.bind("<Motion>", lambda event:movingMouse(event,my_canvas,app))
app.bind("<ButtonRelease-1>", lambda event:endMoving(event,my_canvas,app))
app.bind("<Double-Button-1>", lambda event:doubleClickHandler(event,my_canvas,app))
app.bind("<Key>", lambda event:keyHandler(event,my_canvas,app))
app.bind("<MouseWheel>", lambda event:do_zoom(event,my_canvas))
app.bind("<Button-1>",lambda event:clickHandler(event,my_canvas))

draw_init_blocks(my_canvas,app)

app.mainloop()