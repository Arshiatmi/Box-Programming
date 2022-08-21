from Utils.variables import Variable
from .exceptions import *
from .enums import *
from .global_vars import *

# Options That Every Function Must Have.


class Option:
    def __init__(self, text: str, Type: Types, Side: Sides = None):
        global options
        options[text] = self
        self.type = Type
        self.key = text
        self.side = Side
        self.variable = Variable(text, Type)
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

    def get_input_types(self) -> list:
        ans = []
        for i in self.inputs:
            ans.append(i.type)
        return ans

    def get_output_types(self) -> list:
        ans = []
        for i in self.outputs:
            ans.append(i.type)
        return ans

    def has_this_inputs(self, input_types: dict) -> bool:
        for i in self.inputs:
            target_type = i.type
            if i.type in Variable.VariableTypes:
                target_type = Types.variable
            if target_type not in input_types:
                return False
            input_types[target_type] -= 1
            input_types = {k: v for k, v in input_types.items() if v > 0}
        if not input_types:
            return False
        return True

    def has_this_outputs(self, output_types: dict) -> bool:
        for i in self.outputs:
            target_type = i.type
            if i.type in Variable.VariableTypes:
                target_type = Types.variable
            if target_type not in output_types:
                return False
            output_types[target_type] -= 1
            output_types = {k: v for k, v in output_types.items() if v > 0}
        if not output_types:
            return False
        return True

    def has_any_inputs(self, option_type=None) -> bool:
        if option_type:
            for i in self.inputs:
                if i.type == option_type:
                    return True
            return False
        else:
            return len(self.inputs) > 0

    def has_any_outputs(self, option_type=None) -> bool:
        if option_type:
            for i in self.outputs:
                if i.type == option_type:
                    return True
            return False
        else:
            return len(self.inputs) > 0

    def has_any(self, option_type=None) -> bool:
        if option_type:
            for i in self.outputs:
                if i.type == option_type:
                    return True
            for i in self.inputs:
                if i.type == option_type:
                    return True
            return False
        else:
            return len(self.inputs) > 0

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
            # Set Variable Box
            if self.function.has_this_outputs({Types.variable: 1}) and self.function.has_this_inputs({Types.variable: 1, Types.executable: 1}):
                self.type = Type
            # Get Variable Box
            elif self.function.has_this_outputs({Types.variable: 1}):
                self.type = Type
            # Invalid Variable Box
            else:
                raise IOError("This Format Is Invalid (Should Be Set Or Get).")
        elif Type == BoxTypes.Operator:
            # Normal Operator Functions
            if not self.function.has_any(Types.executable):
                self.type = Type
            else:
                raise IOError("You Should Not Have Any Executable Options.")
        elif Type == BoxTypes.Event:
            # Common Events That Does Not Have Any Inputs
            if not self.function.has_any_inputs():
                self.type = Type
            else:
                raise IOError("Event Boxes Must Not Have Any Inputs.")
        else:
            self.type = Type
        self.inputs = self.function.inputs
        self.outputs = self.function.outputs
        self.tag = name
        self.objects = []
        self.block_input_connected = [None] * len(self.inputs)
        self.block_output_connected = [None] * len(self.outputs)

    def addOption(self, option: Option):
        if self.type == BoxTypes.Executable:
            if option.side == Sides.left:
                self.inputs.append(option)
            elif option.side == Sides.right:
                self.outputs.append(option)
            else:
                raise OptionError(
                    "You Must Define Which Side The Option Is.")
        else:
            raise OptionError("Variable Type Box Can Not Have Options")

    def setFunction(self, func, *args, **argvs):
        if self.type == BoxTypes.Executable:
            self.function = func
            self.function_args = args
            self.function_argvs = argvs
        else:
            raise FunctionError(
                "Variable Type Box Can Not Have A Customize Function")

    def run(self):
        if self.type == BoxTypes.Executable:
            self.function(self.variables, self.inputs, self.outputs, *
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
    def __init__(self, is_drawing=False, index=0) -> None:
        self.is_drawing = is_drawing
        self.index = index
        self.tag = f"Line{self.index}"
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
