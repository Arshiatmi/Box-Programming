from Utils.enums import ConfigModes
from .blocks import conf,Line
from .global_vars import boxes,images
import tkinter as tk

# Mouse Wheel Event
def do_zoom(event,canvas):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    factor = 1.001 ** event.delta
    is_shift = event.state & (1 << 0) != 0
    is_ctrl = event.state & (1 << 2) != 0
    canvas.scale(tk.ALL, x, y, 
                 factor if not is_shift else 1.0, 
                 factor if not is_ctrl else 1.0)

def make_menu(app,ls: dict):
    m = tk.Menu(app, tearoff=0)
    for i,j in ls.items():
        m.add_command(label=i,command=j.function.func)
    return m

def draw_init_blocks(canvas,app):
    global boxes
    boxes["start"].draw_block(app,canvas,(100,100))
    boxes["end"].draw_block(app,canvas,(700,100))

# Line Variables
lines = {}
closest_line_tag = ""
is_dbl_click = False
can_draw_line = False
draw_line_object = None

current_line = Line()

# Click Handler Event
def clickHandler(event,canvas):
    global current_line,is_dbl_click,can_draw_line
    if conf.mode == ConfigModes.normal:
        if can_draw_line:
            coords = (canvas.bbox(draw_line_object))
            x_c = (coords[0] + coords[2]) / 2
            y_c = (coords[1] + coords[3]) / 2
            current_line.start = [x_c,y_c]
            current_line.is_drawing = True
    is_dbl_click = False

# Double Click Event
def doubleClickHandler(event,canvas):
    global current_line,is_dbl_click
    if conf.mode == ConfigModes.line_mode:
        lines[closest_line_tag].remove(canvas)
    is_dbl_click = True

# Moving Mouse When Button 1 Pressed Event
def movingMousePressed(event,canvas,app):
    global closest_line_tag,can_draw_line,draw_line_object
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    closest = canvas.find_closest(x,y)
    closest_tag = canvas.gettags(closest)
    if len(closest_tag[0]) != "temp":
        try:
            canvas.itemconfig(images[closest_tag[0]],image=app.full_execute_image)
            closest_line_tag = closest_tag[0]
            can_draw_line = True
            draw_line_object = images[closest_tag[0]]
        except:
            try:
                canvas.itemconfig(images[closest_line_tag],image=app.empty_execute_image)
                can_draw_line = False
                draw_line_object = None
            except:
                pass
    else:
        try:
            canvas.itemconfig(images[closest_tag[0]],image=app.empty_execute_image)
            can_draw_line = False
            draw_line_object = None
        except:
            try:
                canvas.itemconfig(images[closest_line_tag],image=app.empty_execute_image)
                can_draw_line = False
                draw_line_object = None
            except:
                pass
    if current_line.is_drawing:
        canvas.delete("temp")
        canvas.create_line(current_line.start[0],current_line.start[1],event.x,event.y,tags="temp",width=4,fill='white')

# Set All Lines Width
def set_all_lines_width(canvas,width=1):
    for i in lines.values():
        i.draw_new(canvas,width=width)

# Set A Line Width By Tag
def set_line_width(canvas,line_tag,width=4):
    lines[line_tag].draw_new(canvas,width)

# Mouse Move Event
def movingMouse(event,canvas,app):
    global closest_line_tag,can_draw_line,draw_line_object
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
    elif conf.mode == ConfigModes.normal:
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        closest = canvas.find_closest(x,y)
        closest_tag = canvas.gettags(closest)
        if len(closest_tag) == 2:
            if closest_tag[1] == 'current':
                try:
                    canvas.itemconfig(images[closest_tag[0]],image=app.full_execute_image)
                    closest_line_tag = closest_tag[0]
                    can_draw_line = True
                    draw_line_object = images[closest_tag[0]]
                except:
                    try:
                        canvas.itemconfig(images[closest_line_tag],image=app.empty_execute_image)
                        can_draw_line = False
                        draw_line_object = None
                    except:
                        pass
        else:
            try:
                canvas.itemconfig(images[closest_tag[0]],image=app.empty_execute_image)
                can_draw_line = False
                draw_line_object = None
            except:
                try:
                    canvas.itemconfig(images[closest_line_tag],image=app.empty_execute_image)
                    can_draw_line = False
                    draw_line_object = None
                except:
                    pass


# Key Pressed Event
def keyHandler(event,canvas,app=None):
    if event.char == 'l':
        conf.mode = ConfigModes.line_mode
        set_all_lines_width(canvas,width=1)
    elif event.char == 'b':
        conf.mode = ConfigModes.box_mode
    elif event.char == 'n':
        conf.mode = ConfigModes.normal
        set_all_lines_width(canvas,width=4)
    elif event.keycode == 27:
        if conf.mode == ConfigModes.normal:
            app.quit()
        else:
            conf.mode = ConfigModes.normal
            set_all_lines_width(canvas,width=4)

# Mouse Button 1 Release Event
def endMoving(event,canvas):
    global current_line,can_draw_line
    if not is_dbl_click:
        if conf.mode == ConfigModes.normal:
            if can_draw_line:
                coords = (canvas.bbox(draw_line_object))
                x_c = (coords[0] + coords[2]) / 2
                y_c = (coords[1] + coords[3]) / 2
                current_line.end = [x_c,y_c]
                current_line.is_drawing = False
                canvas.delete("temp")
                canvas.create_line(current_line.start[0],current_line.start[1],current_line.end[0],current_line.end[1],tags=current_line.tag,width=4,fill='white')
                lines[current_line.tag] = (current_line)
                current_line = Line(index=current_line.index + 1)