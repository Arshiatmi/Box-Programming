from .exceptions import *
from .enums import *
from .global_vars import *

# Options That Every Function Must Have.


class Option:
    def __init__(self, text: str, Type: Types):
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
        elif self.type == Types.executable:
            self.input_model = InputTypes.executeButton

# Functions That Are Made Like This To Make Application More Readable


class Function:
    def __init__(self, name, func, inputs=[], outputs=[]) -> None:
        global functions
        functions[name] = self
        self.name = name
        self.func = func
        self.inputs = inputs
        self.outputs = outputs

    def __call__(self, *args: object, **kwds: object) -> None:
        self.func(*args, **kwds)

# Boxes ( Core ) Of This Application


class Box:
    def __init__(self, name="", Type=BoxTypes.Executable, function=Function("pass", lambda x: x)):
        global boxes
        if Type == BoxTypes.Start:
            boxes["start"] = self
            name = "start"
            function = Function("start", lambda x: x, [], [
                                Option("Execute", Types.executable)])
        elif Type == BoxTypes.End:
            boxes["end"] = self
            name = "end"
            function = Function("end", lambda x: x, [
                                Option("Execute", Types.executable)], [])
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
        self.objects = []
        self.block_input_connected = [None] * len(self.inputs)
        self.block_output_connected = [None] * len(self.outputs)

    def addOption(self, option: Option):
        if self.type == BoxTypes.Executable:
            self.options.append(option)
        else:
            raise OptionError("Variable Type Box Can Not Have Options")

    def blockVariables(self, variable: Option):
        if self.type == BoxTypes.Executable:
            self.variables[variable.name] = (variable)
        else:
            self.variables = []
            self.variables[variable.name] = (variable)

    def setFunction(self, func, *args, **argvs):
        if self.type == BoxTypes.Executable:
            self.function = func
            self.function_args = args
            self.function_argvs = argvs
        else:
            raise FunctionError(
                "Variable Type Box Can Not Have A Customize Function")

    def setVariable(self, name, value):
        self.variables[name] = value

    def run(self):
        if self.type == BoxTypes.Executable:
            self.function(self.variables, self.options, *
                          self.function_args, **self.function_argvs)
        else:
            raise FunctionError(
                "Variable Type Box Can Not Have Block Function")

    # It Will Tries To Run A Javascript Code To Draw The Block
    def draw_block(self, startpos: list, endpos=[]):
        pass

    # It Will Tries To Run A Javascript Code To Set Location Of The Block
    def set_location(self, startpos: list, endpos=[]):
        pass

    # It Will Tries To Run A Javascript Code To Move The Block
    def move_block(self, x, y):
        pass

# Line Stuff


class Line:
    def __init__(self, start=[-1, -1], end=[-1, -1], is_drawing=False, index=0, color='white') -> None:
        self.start = start
        self.end = end
        self.is_drawing = is_drawing
        self.index = index
        self.tag = f"Line{self.index}"
        self.removed = False
        self.line_color = color
        self.start_image = None
        self.end_image = None
        self.start_locked = False
        self.end_locked = False
        self.start_box = None
        self.end_box = None

    # It Will Tries To Run A Javascript Code To Draw The Line
    def draw_new(self, canvas, width=4, force=False):
        pass

    # It Will Tries To Run A Javascript Code To Draw The Line
    def draw(self, canvas, width=4, force=False):
        pass

    # It Will Tries To Run A Javascript Code To Remove The Line
    def remove(self, canvas):
        pass
