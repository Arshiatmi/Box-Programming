from Utils.enums import ConfigModes
from .blocks import conf
import tkinter as tk


def make_menu(app,ls: list):
    m = tk.Menu(app, tearoff=0)
    for i in ls:
        m.add_command(label=i.name,command=i.func)
    return m

def draw_blocks(app,block,x,y):
    pass


# Line Variables
lines = {}
closest_line_tag = ""

# Line Stuff
class Line:
    def __init__(self,start=[-1,-1],end=[-1,-1],is_drawing=False,index=0) -> None:
        self.start = start
        self.end = end
        self.is_drawing = is_drawing
        self.index = index
        self.tag = f"Line{self.index}"
        self.removed = False
    
    def draw_new(self,canvas,width=4,force=False):
        if force:
            canvas.delete(self.tag)
            canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1],tags=self.tag,width=width)
        else:
            if not self.removed:
                canvas.delete(self.tag)
                canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1],tags=self.tag,width=width)
    
    def draw(self,canvas,width=4,force=False):
        if force:
            canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1],tags=self.tag,width=width)
        else:
            if not self.removed:
                canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1],tags=self.tag,width=width)
    
    def remove(self,canvas):
        canvas.delete(self.tag)
        self.removed = True

current_line = Line()

# Click Handler Event
def clickHandler(event):
    global current_line
    if conf.mode == ConfigModes.normal:
        current_line.start = [event.x,event.y]
        current_line.is_drawing = True

# Double Click Event
def doubleClickHandler(event,canvas):
    global current_line
    if conf.mode == ConfigModes.line_mode:
        lines[closest_line_tag].remove(canvas)

# Moving Mouse When Button 1 Pressed Event
def movingMousePressed(event,canvas):
    if current_line.is_drawing:
        canvas.delete("temp")
        canvas.create_line(current_line.start[0],current_line.start[1],event.x,event.y,tags="temp",width=4)

# Set All Lines Width
def set_all_lines_width(canvas,width=1):
    for i in lines.values():
        i.draw_new(canvas,width=width)

# Set A Line Width By Tag
def set_line_width(canvas,line_tag,width=4):
    lines[line_tag].draw_new(canvas,width)

# Mouse Move Event
def movingMouse(event,canvas):
    global closest_line_tag
    if conf.mode == ConfigModes.line_mode:
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        closest = canvas.find_closest(x,y)
        closest = canvas.gettags(closest)
        if len(closest) >= 1:
            if (closest[0]) != closest_line_tag:
                set_all_lines_width(canvas)
                closest_line_tag = closest[0]
                set_line_width(canvas,closest[0])

# Key Pressed Event
def keyHandler(event,canvas):
    if event.char == 'l':
        conf.mode = ConfigModes.line_mode
        set_all_lines_width(canvas,width=1)
    elif event.char == 'b':
        conf.mode = ConfigModes.box_mode
    elif event.char == 'n':
        conf.mode = ConfigModes.normal
        set_all_lines_width(canvas,width=4)

# Mouse Button 1 Release Event
def endMoving(event,canvas):
    global current_line
    if conf.mode == ConfigModes.normal:
        current_line.end = [event.x,event.y]
        current_line.is_drawing = False
        canvas.delete("temp")
        canvas.create_line(current_line.start[0],current_line.start[1],event.x,event.y,tags=current_line.tag,width=4)
        lines[current_line.tag] = (current_line)
        current_line = Line(index=current_line.index + 1)