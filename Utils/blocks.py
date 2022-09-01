from typing import Callable
from Utils.functions import make_id_from_name
from Utils.helpers import convert_to_list
from Utils.variables import Variable, detect_variable_type
from .exceptions import *
from .enums import *
from .global_vars import *

# Options That Every Function Must Have.


class Option:
    Index = 0

    def __init__(self, text: str, Type: Types, Side: Sides = None, variable_mode=False, show_text=False):
        global options
        self.id = make_id_from_name(text)
        self.box_id = self.id
        if Type == Types.executable:
            self.id = "execute_" + self.id
            if Side == Sides.left:
                self.id = self.id + "_in"
            elif Side == Sides.right:
                self.id = self.id + "_out"
        try:
            options[self.id]
            if Type != Types.executable:
                if variable_mode:
                    self.variable = variables[self.id]
                else:
                    self.variable = Variable(self.id, Type)
            Option.Index += 1
            options[self.id + "_" + str(Option.Index)] = self
        except:
            options[self.id] = self
            self.variable = Variable(self.id, Type)
        self.Type = Type
        self.text = text
        self.side = Side
        self.show_text = show_text
        self.parent = None
        self.target_option = None
        if self.Type == Types.boolean:
            self.input_model = InputTypes.checkbox
        elif self.Type == Types.number:
            self.input_model = InputTypes.numberField
        elif self.Type == Types.text:
            self.input_model = InputTypes.textField
        elif self.Type == Types.executable:
            self.input_model = InputTypes.executeButton

    @property
    def value(self):
        if self.Type == Types.executable:
            return self.id
        if self.side == Sides.left:
            if self.target_option:
                self.variable.value = self.target_option.value
        return self.variable.value

    @value.setter
    def value(self, value):
        if self.Type == Types.executable:
            return
        if self.side == Sides.left:
            if self.target_option:
                self.target_option.value = value
                self.variable.value = self.target_option.value
            else:
                self.variable.value = value
        else:
            self.variable.value = value

    def attach(self, option):
        if type(option) == type(self):
            if self.side != option.side:
                self.target_option = option
                self.target_option.target_option = self
                if self.side == Sides.left:
                    self.value = self.target_option.value
                else:
                    self.target_option.value = self.value
            else:
                raise SideError("Sides Should Not Be Equal :(")
        else:
            self.value = option

    def get_box(self):
        if self.parent:
            return self.parent
        else:
            raise BoxError(f"Box With Id {self.box_id} Not Found :(")

    def detach(self):
        self.target_option = None

    def __str__(self):
        return f"Option({self.value})"

    def __repr__(self):
        return f"Option({self.value})"

# Functions That Are Made Like This To Make Application More Readable


class Function:
    Index = 0

    def __init__(self, name: str, func: Callable, inputs: list = [], outputs: list = [], requirements: list = [], is_instance: bool = False) -> None:
        global functions
        self.id = make_id_from_name(name)
        try:
            functions[self.id]
            Function.Index += 1
            functions[self.id + "_" + str(Function.Index)] = self
            if not is_instance:
                logger.warning(
                    f"The Function With id {self.id} Exists. Box id Changed Too {self.id + '_' + str(Function.Index)}")
        except:
            functions[self.id] = self
        self.name = name
        self.func = func
        self.inputs = inputs
        self.outputs = outputs
        self.requirements = requirements

    def get_input_types(self) -> list:
        ans = []
        for i in self.inputs:
            ans.append(i.Type)
        return ans

    def get_output_types(self) -> list:
        ans = []
        for i in self.outputs:
            ans.append(i.Type)
        return ans

    def has_this_inputs(self, input_types: dict) -> bool:
        for i in self.inputs:
            target_type = i.Type
            if i.Type in Variable.VariableTypes:
                target_type = Types.variable
            if target_type not in input_types:
                return False
            input_types[target_type] -= 1
            input_types = {k: v for k, v in input_types.items() if v > 0}
        if not input_types:
            return True
        return False

    def has_this_outputs(self, output_types: dict) -> bool:
        for i in self.outputs:
            target_type = i.Type
            if i.Type in Variable.VariableTypes:
                target_type = Types.variable
            if target_type not in output_types:
                return False
            output_types[target_type] -= 1
            output_types = {k: v for k, v in output_types.items() if v > 0}
        if not output_types:
            return True
        return False

    def has_any_inputs(self, option_type=None) -> bool:
        if option_type:
            for i in self.inputs:
                if i.Type == option_type:
                    return True
            return False
        else:
            return len(self.inputs) > 0

    def has_any_outputs(self, option_type=None) -> bool:
        if option_type:
            for i in self.outputs:
                if i.Type == option_type:
                    return True
            return False
        else:
            return len(self.inputs) > 0

    def has_any(self, option_type=None) -> bool:
        if option_type:
            for i in self.outputs:
                if i.Type == option_type:
                    return True
            for i in self.inputs:
                if i.Type == option_type:
                    return True
            return False
        else:
            return len(self.inputs) > 0

    def __call__(self, *args: object, **kwds: object) -> None:
        return self.func(*args, **kwds)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Function({self.id})"

# Boxes ( Core ) Of This Application


class Box:
    Index = 0

    def __init__(self, name: str = "", Type: BoxTypes = BoxTypes.Executable, function: Function = Function("pass", lambda x: x), is_instance: bool = False):
        global boxes
        if Type == BoxTypes.Start:
            boxes["start"] = self
            name = "start"
            function = Function("start", lambda x: x, [], [
                                Option("StartExecute", Types.executable)])
        elif Type == BoxTypes.End:
            boxes["end"] = self
            name = "end"
            function = Function("end", lambda x: x, [
                Option("EndExecute", Types.executable)], [])
        elif name:
            self.id = make_id_from_name(name)
            try:
                boxes[self.id]
                Box.Index += 1
                boxes[self.id + "_" + str(Box.Index)] = self
                if not is_instance:
                    logger.warning(
                        f"The Box With id {self.id} Exists. Box id Changed Too {self.id + '_' + str(Box.Index)}")
            except:
                boxes[self.id] = self
        else:
            raise ValueError("Box Must Have A Name.")
        self.name = name
        self.function = function
        self.function_args = None
        self.function_argvs = None
        self._function_inputs = []
        self._function_outputs = []
        self.x = None
        self.y = None
        if Type == BoxTypes.Variable:
            # Set Variable Box
            if self.function.has_this_outputs({Types.executable: 1}) and self.function.has_this_inputs({Types.variable: 1, Types.executable: 1}):
                self.Type = Type
            # Get Variable Box
            elif self.function.has_this_outputs({Types.variable: 1}):
                self.Type = Type
            # Invalid Variable Box
            else:
                raise IOError("This Format Is Invalid (Should Be Set Or Get).")
        elif Type == BoxTypes.Operator:
            # Normal Operator Functions
            if not self.function.has_any(Types.executable):
                self.Type = Type
            else:
                raise IOError("You Should Not Have Any Executable Options.")
        elif Type == BoxTypes.Event:
            # Common Events That Does Not Have Any Inputs
            if not self.function.has_any_inputs():
                self.Type = Type
            else:
                raise IOError("Event Boxes Must Not Have Any Inputs.")
        else:
            self.Type = Type
        self.inputs = self.function.inputs
        self.outputs = self.function.outputs
        self.block_input_connected = [None] * len(self.inputs)
        self.block_output_connected = [None] * len(self.outputs)
        for i in self.inputs:
            i.parent = self
        for i in self.outputs:
            i.parent = self

    @property
    def function_inputs(self):
        return self._function_inputs

    @function_inputs.setter
    def function_inputs(self, value):
        self._function_inputs = value
        refrence_types = list(filter(lambda x: x.Type in Variable.VariableTypes or x.Type ==
                                     Types.variable, self.inputs))
        if len(value) == len(refrence_types):
            for c, i in enumerate(refrence_types):
                try:
                    i.value = value[c].value
                except:
                    i.value = value[c]

    @property
    def function_outputs(self):
        return self._function_outputs

    @function_outputs.setter
    def function_outputs(self, value):
        self._function_outputs = value
        refrence_types = list(filter(lambda x: x.Type in Variable.VariableTypes or x.Type ==
                                     Types.variable, self.outputs))
        if len(value) == len(refrence_types):
            for c, i in enumerate(refrence_types):
                try:
                    i.value = value[c].value
                except:
                    i.value = value[c]

    def addOption(self, option: Option):
        if self.Type == BoxTypes.Executable:
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
        if self.Type == BoxTypes.Executable:
            self.function = func
            self.function_args = args
            self.function_argvs = argvs
        else:
            raise FunctionError(
                "Variable Type Box Can Not Have A Customize Function")

    def check_types(self, refrence_types: list, types_to_check: list) -> bool:
        refrence_types = list(filter(lambda x: x.Type in Variable.VariableTypes or x.Type ==
                                     Types.variable, refrence_types))
        for i, j in zip(refrence_types, types_to_check):
            if i.Type == detect_variable_type(j, return_variable_type=False):
                continue
            return False
        return True

    def attach(self, box, self_index, target_index_or_value, side=Sides.left):
        if box == None:
            if side == Sides.left:  # Side Of Line
                self.inputs[self_index].attach(target_index_or_value)
            else:
                self.outputs[self_index].attach(target_index_or_value)
        else:
            if side == Sides.left:  # Side Of Line
                self.inputs[self_index].attach(
                    box.outputs[target_index_or_value])
            else:
                self.outputs[self_index].attach(
                    box.inputs[target_index_or_value])
        if self.Type == BoxTypes.Operator:
            self()

    def detach(self, box, self_index, target_index_or_value, side=Sides.left):
        if box == None:
            if side == Sides.left:  # Side Of Line
                self.inputs[self_index].detach()
            else:
                self.outputs[self_index].detach()
        else:
            if side == Sides.left:  # Side Of Line
                self.inputs[self_index].detach()
                box.outputs[target_index_or_value].detach()
            else:
                self.outputs[self_index].detach()
                box.inputs[target_index_or_value].detach()
        if self.Type == BoxTypes.Operator:
            self()

    def __call__(self, *args):
        if self.Type in [BoxTypes.Executable, BoxTypes.Variable, BoxTypes.Operator]:
            if self.check_types(self.inputs, args):
                self.function_inputs = args
                ans = self.function(self.function.id, self.inputs, self.outputs,
                                    *args)
                ans = convert_to_list(ans)
                if self.check_types(self.outputs, ans):
                    self.function_outputs = ans
                    if self.Type == BoxTypes.Operator:
                        if len(ans) == 1:
                            try:
                                return ans[0].value
                            except:
                                return ans[0]
                    else:
                        if len(ans) == 1:
                            return ans[0]
                    return list(map(lambda x: x.value, self.function_outputs))
                raise FunctionError(
                    "Function Outputs Are Not Defined In Correct Type.")
            else:
                raise TypeError("Inputs Are Not Valid.")
        else:
            raise FunctionError(
                "BoxType Must Be Executable To Be Called")

    def get_connected_option(self):
        ans = self()
        return ans.target_option

    def execute_box(self):
        ans = self()
        return ans.target_option.parent

    def __str__(self) -> str:
        return f"Box({self.name})"

    def __repr__(self) -> str:
        return f"Box({self.name})"

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
    Index = 0

    def __init__(self) -> None:
        self.id = f"Line{Line.Index}"
        Line.Index += 1
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
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
