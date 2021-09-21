from Utils.enums import ConfigModes, Current
from .blocks import conf,Line
from .global_vars import ALL_GLOBALS, boxes,images,locked_image_objects
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
    boxes["start"].draw_block((100,100))
    boxes["end"].draw_block((700,100))

# Line Variables
lines = {}
closest_line_tag = ""
is_dbl_click = False
can_draw_line = False
can_move_box = False
draw_object = None
moving_object = None

current_line = Line()

# Click Handler Event
def clickHandler(event,canvas):
    global current_line,is_dbl_click,can_draw_line,moving_object
    if conf.mode == ConfigModes.normal:
        if can_draw_line:
            coords = (canvas.bbox(draw_object))
            x_c = (coords[0] + coords[2]) / 2
            y_c = (coords[1] + coords[3]) / 2
            current_line.start = [x_c,y_c]
            current_line.is_drawing = True
            current_line.start_image = draw_object
            current_line.start_locked = True
            current_line.start_box = canvas.find_withtag(canvas.gettags(draw_object)[0].replace("exeout",""))
            # conf.current = Current.line
            locked_image_objects.append(draw_object)
        elif can_move_box:
            coords = (canvas.bbox(draw_object))
            x_c = (coords[0] + coords[2]) / 2
            y_c = (coords[1] + coords[3]) / 2
            moving_object = boxes[draw_object]
    is_dbl_click = False

# Double Click Event
def doubleClickHandler(event,canvas,app):
    global current_line,is_dbl_click
    if conf.mode == ConfigModes.line_mode:
        lines[closest_line_tag].remove(canvas)
        lines[closest_line_tag].start_locked = False
        lines[closest_line_tag].end_locked = False
        locked_image_objects.remove(lines[closest_line_tag].start_image)
        locked_image_objects.remove(lines[closest_line_tag].end_image)
        start_img = canvas.gettags(lines[closest_line_tag].start_image)[0]
        end_img = canvas.gettags(lines[closest_line_tag].end_image)[0]
        canvas.itemconfig(images[start_img],image=app.empty_execute_image)
        canvas.itemconfig(images[end_img],image=app.empty_execute_image)
    is_dbl_click = True

# Moving Mouse When Button 1 Pressed Event
def movingMousePressed(event,canvas,app):
    global closest_line_tag,can_draw_line,draw_object,can_move_box,moving_object
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    closest = canvas.find_closest(x,y)
    closest_tag = canvas.gettags(closest)
    for i in locked_image_objects:
        canvas.itemconfig(i,image=app.full_execute_image)
    try:
        if closest[0] not in locked_image_objects:
            if len(closest_tag[0]) != "temp":
                if closest_tag[0].endswith("exein") or closest_tag[0].endswith("exeout"):
                    try:
                        canvas.itemconfig(images[closest_tag[0]],image=app.full_execute_image)
                        closest_line_tag = closest_tag[0]
                        can_draw_line = True
                        draw_object = images[closest_tag[0]]
                    except:
                        try:
                            canvas.itemconfig(images[closest_tag[0]],image=app.empty_execute_image)
                            can_draw_line = False
                            draw_object = None
                        except:
                            pass
                else:
                    for i in images:
                        if i not in locked_image_objects:
                            canvas.itemconfig(images[closest_tag[0]],image=app.empty_execute_image)
            else:
                try:
                    canvas.itemconfig(images[closest_tag[0]],image=app.empty_execute_image)
                    can_draw_line = False
                    draw_object = None
                except:
                    try:
                        canvas.itemconfig(images[closest_tag[0]],image=app.empty_execute_image)
                        can_draw_line = False
                        draw_object = None
                    except:
                        pass
            # else:
            #     canvas.itemconfig(images[closest_tag[0]],image=app.full_execute_image)
    except:
        pass
    if current_line.is_drawing:
        canvas.delete("temp")
        canvas.create_line(current_line.start[0],current_line.start[1],event.x,event.y,tags="temp",width=4,fill='white')
    else:
        if can_move_box and moving_object:
            moving_object.set_location((x,y))

# Set All Lines Width
def set_all_lines_width(canvas,width=1):
    for i in lines.values():
        i.draw_new(canvas,width=width)

# Set A Line Width By Tag
def set_line_width(canvas,line_tag,width=4):
    try:
        lines[line_tag].draw_new(canvas,width)
    except KeyError:
        pass

# Mouse Move Event
def movingMouse(event,canvas,app):
    global closest_line_tag,can_draw_line,draw_object,can_move_box,moving_object
    for i in locked_image_objects:
        canvas.itemconfig(i,image=app.full_execute_image)
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
        if moving_object and can_move_box:
            moving_object = None
            can_move_box = False
        try:
            if closest[0] not in locked_image_objects:
                if len(closest_tag) == 2 and closest_tag[1] == 'current':
                    if closest_tag[0].endswith("exein") or closest_tag[0].endswith("exeout") :
                        try:
                            canvas.itemconfig(images[closest_tag[0]],image=app.full_execute_image)
                            closest_line_tag = closest_tag[0]
                            can_draw_line = True
                            draw_object = images[closest_tag[0]]
                        except:
                            try:
                                canvas.itemconfig(images[closest_tag[0]],image=app.empty_execute_image)
                                can_draw_line = False
                                draw_object = None
                            except:
                                pass
                    elif closest_tag[0].endswith("txt"):
                        pass
                    else:
                        try:
                            for i in images:
                                var = canvas.find_withtag(i)
                                if var[0] not in locked_image_objects:
                                    canvas.itemconfig(images[closest_tag[0]],image=app.empty_execute_image)
                        except:
                            pass
                        # Check If Closest Is Actually A Box
                        try:
                            o1 = images.get(closest_tag[0] + "exein","")
                            o2 = images.get(closest_tag[0] + "exeout","")
                            if not o1 and not o2:
                                raise
                            can_move_box = True
                            draw_object = closest_tag[0]
                        except:
                            pass
                else:
                    try:
                        for i in images:
                            var = canvas.find_withtag(i)
                            if var[0] not in locked_image_objects:
                                canvas.itemconfig(images[i],image=app.empty_execute_image)
                        can_draw_line = False
                        draw_object = None
                    except:
                        pass
        except:
            pass
    elif conf.mode == ConfigModes.box_mode:
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
def endMoving(event,canvas,app):
    global current_line,can_draw_line,locked_image_objects
    for i in locked_image_objects:
        canvas.itemconfig(i,image=app.full_execute_image)
    if not is_dbl_click:
        if conf.mode == ConfigModes.normal:
            if can_draw_line:
                coords = (canvas.bbox(draw_object))
                x_c = (coords[0] + coords[2]) / 2
                y_c = (coords[1] + coords[3]) / 2
                current_line.end = [x_c,y_c]
                current_line.is_drawing = False
                current_line.end_image = draw_object
                current_line.end_locked = True
                current_line.end_box = canvas.find_withtag(canvas.gettags(draw_object)[0].replace("exein",""))
                locked_image_objects.append(draw_object)
                canvas.delete("temp")
                canvas.create_line(current_line.start[0],current_line.start[1],current_line.end[0],current_line.end[1],tags=current_line.tag,width=4,fill='white')
                lines[current_line.tag] = (current_line)
                current_line = Line(index=current_line.index + 1)
            # else:
            #     boxes["start"].move_block(10,10)

def init_builtins():
    import Utils.builtins