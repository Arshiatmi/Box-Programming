from Utils.enums import BoxTypes, OperatorBuiltins
from Utils.blocks import Box
from Utils.exceptions import BoxError
from Utils.operators import *

Box(Type=BoxTypes.Start)
Box(Type=BoxTypes.End)

variable_funcs = {
    Types.boolean: [getBooleanVariable, setBooleanVariable, "Boolean"],
    Types.number: [getNumberVariable, setNumberVariable, "Number"],
    Types.text: [getTextVariable, setTextVariable, "String"],
}


def define_variable(name, Type):
    get_variable = Function(f"Function Get {name}",
                            variable_funcs[Type][0], [], [Option(f"{name}", Type, Sides.right)])

    set_variable = Function(f"Function Set {name}",
                            variable_funcs[Type][1], [Option(f"Execute_{name}_in", Types.executable, Sides.left), Option(f"{name}", Type, Sides.left)], [Option(f"Execute_{name}_out", Types.executable, Sides.right)])

    box_get_variable = Box(f"Get {variable_funcs[Type][2]} Variable",
                           BoxTypes.Variable, get_variable)
    box_set_variable = Box(f"Set {variable_funcs[Type][2]} Variable",
                           BoxTypes.Variable, set_variable)
    return box_get_variable, box_set_variable


def make_box(builtin_Box_Type, Type):
    if Type == BoxTypes.Operator:
        if builtin_Box_Type == OperatorBuiltins.Add_Two_Numbers:
            return Box("Add Two Numbers", BoxTypes.Operator, add_two_numbers_operator)
        elif builtin_Box_Type == OperatorBuiltins.Add_Two_Text:
            return Box("Add Two Text", BoxTypes.Operator, add_two_text_operator)
        elif builtin_Box_Type == OperatorBuiltins.Minus_Two_Numbers:
            return Box("Minus Two Numbers", BoxTypes.Operator, minus_two_numbers_operator)
        elif builtin_Box_Type == OperatorBuiltins.AND:
            return Box("AND", BoxTypes.Operator, AND_operator)
        elif builtin_Box_Type == OperatorBuiltins.OR:
            return Box("OR", BoxTypes.Operator, OR_operator)
        else:
            raise BoxError("The Operator Box Type Is Not Defined.")
