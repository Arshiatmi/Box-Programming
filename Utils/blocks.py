from .exceptions import *
from .enums import *
from .functions import setOptions

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

class Function:
    def __init__(self,name,func) -> None:
        self.name = name
        self.func = func
    
    def __call__(self, *args: object, **kwds: object) -> None:
        self.func(*args,**kwds)

class Box:
    def __init__(self,Type=BoxTypes.Executable,inputs=[],outputs=[]):
        self.function = setOptions
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