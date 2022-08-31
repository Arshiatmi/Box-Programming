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
    target_id = make_id_from_name(name)
    get_variable = Function(f"Function Get {target_id}",
                            variable_funcs[Type][0], [], [Option(f"{target_id}", Type, Sides.right, variable_mode=True)])

    set_variable = Function(f"Function Set {target_id}",
                            variable_funcs[Type][1], [Option(f"{target_id}", Types.executable, Sides.left), Option(f"{target_id}", Type, Sides.left, variable_mode=True)], [Option(f"{target_id}", Types.executable, Sides.right)])

    box_get_variable = Box(f"Get {variable_funcs[Type][2]} Variable ({target_id})",
                           BoxTypes.Variable, get_variable)
    box_set_variable = Box(f"Set {variable_funcs[Type][2]} Variable ({target_id})",
                           BoxTypes.Variable, set_variable)
    return box_get_variable, box_set_variable


def make_box(builtin_Box_Type, Type):
    if Type == BoxTypes.Operator:
        if builtin_Box_Type == OperatorBuiltins.Add_Two_Numbers:
            return Box("Add Two Numbers", BoxTypes.Operator, add_two_numbers_operator, True)
        elif builtin_Box_Type == OperatorBuiltins.Add_Two_Text:
            return Box("Add Two Text", BoxTypes.Operator, add_two_text_operator, True)
        elif builtin_Box_Type == OperatorBuiltins.Minus_Two_Numbers:
            return Box("Minus Two Numbers", BoxTypes.Operator, minus_two_numbers_operator, True)
        elif builtin_Box_Type == OperatorBuiltins.AND:
            return Box("AND", BoxTypes.Operator, AND_operator, True)
        elif builtin_Box_Type == OperatorBuiltins.OR:
            return Box("OR", BoxTypes.Operator, OR_operator, True)
        else:
            raise BoxError("The Operator Box Type Is Not Defined.")
