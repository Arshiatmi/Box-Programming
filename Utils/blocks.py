from .exceptions import *
from .enums import *

# Options That Every Function Must Have.
class Option:
    def __init__(self,text: str,Type: Types):
        self.type = Type
        self.key = text
        if self.type == Types.boolean:
            self.input_model = InputTypes.checkbox
        elif self.type == Types.number:
            self.input_model = InputTypes.numberField
        elif self.type == Types.string:
            self.input_model = InputTypes.textField

# Functions That Are Made Like This To Make Application More Readable
class Function:
    def __init__(self,name,func) -> None:
        self.name = name
        self.func = func
    
    def __call__(self, *args: object, **kwds: object) -> None:
        self.func(*args,**kwds)

# Boxes ( Core ) Of This Application
class Box:
    def __init__(self,Type=BoxTypes.Executable,inputs=[],outputs=[]):
        self.function = None
        self.function_args = None
        self.function_argvs = None
        if Type == BoxTypes.Variable:
            if len(inputs) == 1 and len(outputs) == 0:
                self.type = Type
            else:
                raise IOError("You Must Define 1 input And No Outputs.")
        else:
            self.type = Type
        self.inputs = inputs
        self.outputs = outputs
        self.options = []
        self.variables = {}
    
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
            raise FunctionError("Variable Type Box Can Not Have Block Function")
    
    def setVariable(self,name,value):
        self.variables[name] = value

    def run(self):
        if self.type == BoxTypes.Executable:
            self.function(self.variables,self.options,*self.function_args,**self.function_argvs)
        else:
            raise FunctionError("Variable Type Box Can Not Have Block Function")

# Configs ( For Now Just Mode Of Program )
class Config:
    def __init__(self,mode=ConfigModes.normal):
        self.mode = mode

conf = Config()

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