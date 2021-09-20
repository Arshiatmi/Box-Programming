from .exceptions import *
from .enums import *
from .global_vars import *

# Options That Every Function Must Have.
class Option:
    def __init__(self,text: str,Type: Types):
        global options
        options[text] = self
        self.type = Type
        self.key = text
        if self.type == Types.boolean:
            self.input_model = InputTypes.checkbox
        elif self.type == Types.number:
            self.input_model = InputTypes.numberField
        elif self.type == Types.text:
            self.input_model = InputTypes.textField

# Functions That Are Made Like This To Make Application More Readable
class Function:
    def __init__(self,name,func,inputs=[],outputs=[]) -> None:
        global functions
        functions[name] = self
        self.name = name
        self.func = func
        self.inputs = inputs
        self.outputs = outputs
    
    def __call__(self, *args: object, **kwds: object) -> None:
        self.func(*args,**kwds)

# Boxes ( Core ) Of This Application
class Box:
    def __init__(self,name="",Type=BoxTypes.Executable,function=Function("pass",lambda x:x)):
        global boxes
        if Type == BoxTypes.Start:
            boxes["start"] = self
            name = "Start"
            function = Function("start",lambda x:x,[],[Option("Execute",Types.executable)])
        elif Type == BoxTypes.End:
            boxes["end"] = self
            name = "Exit"
            function = Function("end",lambda x:x,[Option("Execute",Types.executable)],[])
        elif name:
            boxes[name] = self
        else:
            boxes[function.name] = self
        self.name = name
        self.function = function
        self.function_args = None
        self.function_argvs = None
        if Type == BoxTypes.Variable:
            if len(self.function.inputs) == 1 and len(self.function.outputs) == 1:
                self.type = Type
            else:
                raise IOError("You Must Define 1 input And 1 Outputs.")
        else:
            self.type = Type
        self.inputs = self.function.inputs
        self.outputs = self.function.outputs
        self.options = []
        self.variables = {}
        self.tag = name
        
    
    def blockOptions(self,option: Option):
        if self.type == BoxTypes.Executable:
            self.options.append(option)
        else:
            raise OptionError("Variable Type Box Can Not Have Options")
    
    def blockVariables(self,variable: Option):
        if self.type == BoxTypes.Executable:
            self.variables[variable.name] = (variable)
        else:
            self.variables = []
            self.variables[variable.name] = (variable)

    def blockFunction(self,func,*args,**argvs):
        if self.type == BoxTypes.Executable:
            self.function = func
            self.function_args = args
            self.function_argvs = argvs
        else:
            raise FunctionError("Variable Type Box Can Not Have A Customize Function")
    
    def setVariable(self,name,value):
        self.variables[name] = value

    def run(self):
        if self.type == BoxTypes.Executable:
            self.function(self.variables,self.options,*self.function_args,**self.function_argvs)
        else:
            raise FunctionError("Variable Type Box Can Not Have Block Function")
    
    def draw_block(self,app,canvas,startpos: list,endpos=[]):
        if not endpos:
            endpos = (startpos[0] + 200,startpos[1] + 100)
        canvas.create_rectangle(startpos[0],startpos[1],endpos[0],endpos[1] + (max(len(self.inputs),len(self.outputs)) * 100),fill='black',tags=self.name)
        canvas.pack()
        canvas.create_text(startpos[0] + 80,startpos[1] + 10,fill="white",font="Times 14 italic bold",text=self.name)
        for i in self.inputs:
            if i.type == Types.executable:
                images[self.name + "exein"] = (canvas.create_image(startpos[0] + 30,startpos[1] + 30,image=app.empty_execute_image,tags=self.name + "exein"))
        for i in self.outputs:
            if i.type == Types.executable:
                images[self.name + "exeout"] = (canvas.create_image(endpos[0] - 30,endpos[1] - 70,image=app.empty_execute_image,tags=self.name + "exeout"))

# Configs ( For Now Just Mode Of Program )
class Config:
    def __init__(self,mode=ConfigModes.normal):
        self.mode = mode

conf = Config()

# Line Stuff
class Line:
    def __init__(self,start=[-1,-1],end=[-1,-1],is_drawing=False,index=0,color='white') -> None:
        self.start = start
        self.end = end
        self.is_drawing = is_drawing
        self.index = index
        self.tag = f"Line{self.index}"
        self.removed = False
        self.line_color = color
    
    def draw_new(self,canvas,width=4,force=False):
        if force:
            canvas.delete(self.tag)
            canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1],tags=self.tag,width=width,fill=self.line_color)
        else:
            if not self.removed:
                canvas.delete(self.tag)
                canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1],tags=self.tag,width=width,fill=self.line_color)
    
    def draw(self,canvas,width=4,force=False):
        if force:
            canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1],tags=self.tag,width=width,fill=self.line_color)
        else:
            if not self.removed:
                canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1],tags=self.tag,width=width,fill=self.line_color)
    
    def remove(self,canvas):
        canvas.delete(self.tag)
        self.removed = True