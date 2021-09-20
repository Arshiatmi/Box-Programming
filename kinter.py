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

# class BoxPanel(tk.Frame):
#     def __init__(self, master):
#         self.master = master
#         super().__init__(self.master)

#         self.myFont = font.Font(family='Helvetica', size=36, weight='bold')

#         self.actions = tuple([self.before,self.after])
#         self.buttons = []
#         self.make_buttons()
#         self.pack(fill=tk.BOTH, expand=True)

#     def make_buttons(self):
#         btn_idx = 0
#         action = self.actions[btn_idx]
#         imgpath = 'imgs/ok/empty.png'
#         photo = tk.PhotoImage(file = imgpath)
#         b_text = f"Button {btn_idx + 1}"
#         b = tk.Button(self, 
#                         text=b_text,
#                         font=self.myFont, 
#                         command=action, 
#                         height=2, width=6,
#                         image=photo)
#         b.grid(row=1, column=1, padx=20)
#         self.buttons.append(b)
#         btn_idx += 1
#         self.buttons = tuple(self.buttons)


#     def before(self):
#         print("Alert Button 1 Pressed")

#     def after(self):
#         print("Alert Button 2 Pressed")

#     def alert_cycle_3_to_8(self):
#         print("Alert Button 3 to 8 Pressed")

#     def _quit(self):
#         self.master.destroy()


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


# go = tk.Button(master=back, text='Start Game', command=startgame)
# go.pack()
# close = tk.Button(master=back, text='Quit', command=app.destroy)
# close.pack()
# info = tk.Label(master=back, text='Made by me!', bg='red', fg='black')
# info.pack()

# app1 = BoxPanel(app)

# tk.Label(app, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white").place(x=5, y=0)
# tk.Label(app, text="Position 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
# tk.Label(app, text="Position 3 : x=75, y=80", bg="#FF0099", fg="white").place(x=75, y=80)

app.mainloop()