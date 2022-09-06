from Utils.enums import ArrayBuiltins, BoxTypes, CastBuiltins, ExecutableBuiltins, FileBuiltins, OperatorBuiltins, TextBuiltins
from Utils.blocks import Box
from Utils.exceptions import BoxError
from Utils.box_functions import *

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
        # Operators
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
        # Executable Boxes
        if builtin_Box_Type in ExecutableBuiltins:
            if builtin_Box_Type == ExecutableBuiltins.If:
                return Box("if", BoxTypes.Executable, if_statement_function(), True)
            elif builtin_Box_Type == ExecutableBuiltins.Input:
                return Box("Input", BoxTypes.Executable, get_input_function(), True)
            elif builtin_Box_Type == ExecutableBuiltins.Print:
                return Box("Print", BoxTypes.Executable, print_string_function(), True)
            elif builtin_Box_Type == ExecutableBuiltins.For:
                return Box("For", BoxTypes.Executable, for_loop_function(), True)

        # Type Cast Boxes
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
            elif builtin_Box_Type == CastBuiltins.Variable_To_Text:
                return Box("Cast Any Variable Type To Text", BoxTypes.Executable, variable_to_text_function(), True)

        # Arrays
        elif builtin_Box_Type in ArrayBuiltins:
            if builtin_Box_Type == ArrayBuiltins.Parse:
                return Box("Array Parse", BoxTypes.Executable, parse_array_function(), True, auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Append:
                return Box("Array Append", BoxTypes.Executable, append_array_function(), True, auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Prepend:
                return Box("Array Prepend", BoxTypes.Executable, prepend_array_function(), True, auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Count:
                return Box("Array Count Of Element", BoxTypes.Executable, count_elements_array_function(), True, auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Index:
                return Box("Array Index Of Elemenet", BoxTypes.Executable, index_element_array_function(), True, auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Insert:
                return Box("Array Insert Data", BoxTypes.Executable, insert_element_array_function(), True, auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Remove:
                return Box("Array Remove Element/Index", BoxTypes.Executable, remove_element_array_function(), True, auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Sort:
                return Box("Array Sort", BoxTypes.Executable, sort_array_function(), True, auto_run=True)

        # Files
        elif builtin_Box_Type in FileBuiltins:
            if builtin_Box_Type == FileBuiltins.ReadFile:
                return Box("Read File", BoxTypes.Executable, read_file_function(), True)
            if builtin_Box_Type == FileBuiltins.WriteFile:
                return Box("Write File", BoxTypes.Executable, write_file_function(), True)
            if builtin_Box_Type == FileBuiltins.RemoveFile:
                return Box("Remove File", BoxTypes.Executable, delete_file_function(), True)
            if builtin_Box_Type == FileBuiltins.FileList:
                return Box("Get File List", BoxTypes.Executable, file_list_function(), True)

        # Texts
        elif builtin_Box_Type in TextBuiltins:
            if builtin_Box_Type == TextBuiltins.Capitalize:
                return Box("Text Capitalize", BoxTypes.Executable, capitalize_text_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.Count:
                return Box("Text Count", BoxTypes.Executable, count_text_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.EndsWith:
                return Box("Text Endswith", BoxTypes.Executable, endswith_text_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.Find:
                return Box("Text Find", BoxTypes.Executable, find_text_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsAlphabet:
                return Box("Text Is Alphabet", BoxTypes.Executable, isalphabet_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsAlphabetNumber:
                return Box("Text Is Alphabet Or Number Or Both", BoxTypes.Executable, isalphabetnumber_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsDigit:
                return Box("Text Is Digits ( Number )", BoxTypes.Executable, isdigits_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsUpperCase:
                return Box("Text Is Uppercase", BoxTypes.Executable, isupper_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsLowerCase:
                return Box("Text Is Lowercase", BoxTypes.Executable, islower_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.ToUpper:
                return Box("Text To Uppercase", BoxTypes.Executable, toupper_function(), True, auto_run=True)
            elif builtin_Box_Type == TextBuiltins.ToLower:
                return Box("Text To Lowercase", BoxTypes.Executable, tolower_function(), True, auto_run=True)
