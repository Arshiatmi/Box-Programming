import tkinter as tk


def make_menu(app,ls: list):
    m = tk.Menu(app, tearoff=0)
    for i in ls:
        m.add_command(label=i.name,command=i.func)
    return m

def draw_blocks(app,block,x,y):
    pass