from Utils.enums import ArrayBuiltins, BoxTypes, CastBuiltins, ExecutableBuiltins, OperatorBuiltins
from Utils.blocks import Box
from Utils.exceptions import BoxError
from Utils.operators import *

Box(Type=BoxTypes.Start)
Box(Type=BoxTypes.End)

variable_funcs = {
    Types.boolean: [getBooleanVariable, setBooleanVariable, "Boolean"],
    Types.number: [getNumberVariable, setNumberVariable, "Number"],
    Types.text: [getTextVariable, setTextVariable, "String"],
    Types.array: [getArrayVariable, setArrayVariable, "Array"],
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


def make_box(builtin_Box_Type, Type: BoxTypes):
    if Type == BoxTypes.Operator:
        if builtin_Box_Type == OperatorBuiltins.Add_Two_Numbers:
            return Box("Add Two Numbers", BoxTypes.Operator, add_two_numbers_operator(), True)
        elif builtin_Box_Type == OperatorBuiltins.Add_Two_Text:
            return Box("Add Two Text", BoxTypes.Operator, add_two_text_operator(), True)
        elif builtin_Box_Type == OperatorBuiltins.Minus_Two_Numbers:
            return Box("Minus Two Numbers", BoxTypes.Operator, minus_two_numbers_operator(), True)
        elif builtin_Box_Type == OperatorBuiltins.AND:
            return Box("AND", BoxTypes.Operator, AND_operator(), True)
        elif builtin_Box_Type == OperatorBuiltins.OR:
            return Box("OR", BoxTypes.Operator, OR_operator(), True)
        else:
            raise BoxError("The Operator Box Type Is Not Defined.")
    elif Type == BoxTypes.Executable:
        if builtin_Box_Type == ExecutableBuiltins.If:
            return Box("if", BoxTypes.Executable, if_statement_function(), True)
        elif builtin_Box_Type == ExecutableBuiltins.Input:
            return Box("Input", BoxTypes.Executable, get_input_function(), True)
        elif builtin_Box_Type == ExecutableBuiltins.Print:
            return Box("Print", BoxTypes.Executable, print_string_function(), True)
        elif builtin_Box_Type in CastBuiltins:
            if builtin_Box_Type == CastBuiltins.Number_To_Text:
                return Box("Cast Number To Text", BoxTypes.Executable, number_to_text_function(), True)
            elif builtin_Box_Type == CastBuiltins.Number_To_Bool:
                return Box("Cast Number To Bool", BoxTypes.Executable, number_to_bool_function(), True)
            elif builtin_Box_Type == CastBuiltins.Bool_To_Number:
                return Box("Cast Bool To Number", BoxTypes.Executable, bool_to_number_function(), True)
            elif builtin_Box_Type == CastBuiltins.Bool_To_Text:
                return Box("Cast Bool To Text", BoxTypes.Executable, bool_to_text_function(), True)
            elif builtin_Box_Type == CastBuiltins.Text_To_Number:
                return Box("Cast Text To Number", BoxTypes.Executable, text_to_number_function(), True)
            elif builtin_Box_Type == CastBuiltins.Text_To_Bool:
                return Box("Cast Text To Bool", BoxTypes.Executable, text_to_bool_function(), True)
            elif builtin_Box_Type == CastBuiltins.Array_To_Text:
                return Box("Cast Array To Text", BoxTypes.Executable, array_to_text_function(), True)
            elif builtin_Box_Type == CastBuiltins.Text_To_Array:
                return Box("Cast Text To Array", BoxTypes.Executable, text_to_array_function(), True)
        elif builtin_Box_Type in ArrayBuiltins:
            if builtin_Box_Type == ArrayBuiltins.Parse:
                return Box("Array Parse", BoxTypes.Executable, parse_array_function(), True)
