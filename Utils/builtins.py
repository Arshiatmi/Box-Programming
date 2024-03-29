from Utils.enums import ArrayBuiltins, BoxTypes, Boxfunctions, CastBuiltins, ExecutableBuiltins, FileBuiltins, OperatorBuiltins, Others, TextBuiltins
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
                            variable_funcs[Type][0], [], [Option(f"{target_id}", Type, Sides.right, variable_mode=True)], is_instance=False)

    set_variable = Function(f"Function Set {target_id}",
                            variable_funcs[Type][1], [Option(f"{target_id}", Types.executable, Sides.left), Option(f"{target_id}", Type, Sides.left, variable_mode=True)], [Option(f"{target_id}", Types.executable, Sides.right)], is_instance=False)

    box_get_variable = Box(f"Get {variable_funcs[Type][2]} Variable ({target_id})",
                           BoxTypes.Variable, get_variable, is_instance=False)
    box_set_variable = Box(f"Set {variable_funcs[Type][2]} Variable ({target_id})",
                           BoxTypes.Variable, set_variable, is_instance=False)
    return box_get_variable, box_set_variable


def make_box(builtin_Box_Type, Type: BoxTypes):
    if Type == BoxTypes.Operator:
        # Operators
        if builtin_Box_Type == OperatorBuiltins.Add_Two_Numbers:
            return Box("Add Two Numbers", BoxTypes.Operator, add_two_numbers_operator())
        elif builtin_Box_Type == OperatorBuiltins.Add_Two_Text:
            return Box("Add Two Text", BoxTypes.Operator, add_two_text_operator())
        elif builtin_Box_Type == OperatorBuiltins.Minus_Two_Numbers:
            return Box("Minus Two Numbers", BoxTypes.Operator, minus_two_numbers_operator())
        elif builtin_Box_Type == OperatorBuiltins.AND:
            return Box("AND", BoxTypes.Operator, AND_operator())
        elif builtin_Box_Type == OperatorBuiltins.OR:
            return Box("OR", BoxTypes.Operator, OR_operator())
        elif builtin_Box_Type == OperatorBuiltins.IN:
            return Box("IN", BoxTypes.Operator, IN_operator())
        elif builtin_Box_Type == OperatorBuiltins.POW:
            return Box("POW", BoxTypes.Operator, POW_operator())
        else:
            raise BoxError("The Operator Box Type Is Not Defined.")

    elif Type == BoxTypes.Executable:
        # Executable Boxes
        if builtin_Box_Type in ExecutableBuiltins:
            if builtin_Box_Type == ExecutableBuiltins.If:
                return Box("if", BoxTypes.Executable, if_statement_function())
            elif builtin_Box_Type == ExecutableBuiltins.Input:
                return Box("Input", BoxTypes.Executable, get_input_function())
            elif builtin_Box_Type == ExecutableBuiltins.Print:
                return Box("Print", BoxTypes.Executable, print_string_function())
            elif builtin_Box_Type == ExecutableBuiltins.For:
                return Box("For", BoxTypes.Executable, for_loop_function())

        # Type Cast Boxes
        elif builtin_Box_Type in CastBuiltins:
            if builtin_Box_Type == CastBuiltins.Number_To_Text:
                return Box("Cast Number To Text", BoxTypes.Executable, number_to_text_function())
            elif builtin_Box_Type == CastBuiltins.Number_To_Bool:
                return Box("Cast Number To Bool", BoxTypes.Executable, number_to_bool_function())
            elif builtin_Box_Type == CastBuiltins.Bool_To_Number:
                return Box("Cast Bool To Number", BoxTypes.Executable, bool_to_number_function())
            elif builtin_Box_Type == CastBuiltins.Bool_To_Text:
                return Box("Cast Bool To Text", BoxTypes.Executable, bool_to_text_function())
            elif builtin_Box_Type == CastBuiltins.Text_To_Number:
                return Box("Cast Text To Number", BoxTypes.Executable, text_to_number_function())
            elif builtin_Box_Type == CastBuiltins.Text_To_Bool:
                return Box("Cast Text To Bool", BoxTypes.Executable, text_to_bool_function())
            elif builtin_Box_Type == CastBuiltins.Array_To_Text:
                return Box("Cast Array To Text", BoxTypes.Executable, array_to_text_function())
            elif builtin_Box_Type == CastBuiltins.Text_To_Array:
                return Box("Cast Text To Array", BoxTypes.Executable, text_to_array_function())
            elif builtin_Box_Type == CastBuiltins.Variable_To_Text:
                return Box("Cast Any Variable Type To Text", BoxTypes.Executable, variable_to_text_function())

        # Arrays
        elif builtin_Box_Type in ArrayBuiltins:
            if builtin_Box_Type == ArrayBuiltins.Parse:
                return Box("Array Parse", BoxTypes.Executable, parse_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Append:
                return Box("Array Append", BoxTypes.Executable, append_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Prepend:
                return Box("Array Prepend", BoxTypes.Executable, prepend_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Count:
                return Box("Array Count Of Element", BoxTypes.Executable, count_elements_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Index:
                return Box("Array Index Of Elemenet", BoxTypes.Executable, index_element_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Insert:
                return Box("Array Insert Data", BoxTypes.Executable, insert_element_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Remove:
                return Box("Array Remove Element/Index", BoxTypes.Executable, remove_element_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.Sort:
                return Box("Array Sort", BoxTypes.Executable, sort_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.MinArray:
                return Box("Array Minimum Element", BoxTypes.Executable, get_minimum_in_array_function(), auto_run=True)
            if builtin_Box_Type == ArrayBuiltins.MaxArray:
                return Box("Array Maximum Element", BoxTypes.Executable, get_maximum_in_array_function(), auto_run=True)

        # Files
        elif builtin_Box_Type in FileBuiltins:
            if builtin_Box_Type == FileBuiltins.ReadFile:
                return Box("Read File", BoxTypes.Executable, read_file_function())
            if builtin_Box_Type == FileBuiltins.WriteFile:
                return Box("Write File", BoxTypes.Executable, write_file_function())
            if builtin_Box_Type == FileBuiltins.RemoveFile:
                return Box("Remove File", BoxTypes.Executable, delete_file_function())
            if builtin_Box_Type == FileBuiltins.FileList:
                return Box("Get File List", BoxTypes.Executable, file_list_function())

        # Texts
        elif builtin_Box_Type in TextBuiltins:
            if builtin_Box_Type == TextBuiltins.Capitalize:
                return Box("Text Capitalize", BoxTypes.Executable, capitalize_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.Count:
                return Box("Text Count", BoxTypes.Executable, count_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.EndsWith:
                return Box("Text Endswith", BoxTypes.Executable, endswith_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.Find:
                return Box("Text Find", BoxTypes.Executable, find_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsAlphabet:
                return Box("Text Is Alphabet", BoxTypes.Executable, isalphabet_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsAlphabetNumber:
                return Box("Text Is Alphabet Or Number Or Both", BoxTypes.Executable, isalphabetnumber_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsDigit:
                return Box("Text Is Digits ( Number )", BoxTypes.Executable, isdigits_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsUpperCase:
                return Box("Text Is Uppercase", BoxTypes.Executable, isupper_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.IsLowerCase:
                return Box("Text Is Lowercase", BoxTypes.Executable, islower_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.ToUpper:
                return Box("Text To Uppercase", BoxTypes.Executable, toupper_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.ToLower:
                return Box("Text To Lowercase", BoxTypes.Executable, tolower_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.Join:
                return Box("Text Join Array", BoxTypes.Executable, join_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.Replace:
                return Box("Text Replace", BoxTypes.Executable, replace_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.Strip:
                return Box("Text Strip", BoxTypes.Executable, strip_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.Split:
                return Box("Text Split", BoxTypes.Executable, split_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.SwapCase:
                return Box("Text Swapcase", BoxTypes.Executable, swapcase_text_function(), auto_run=True)
            elif builtin_Box_Type == TextBuiltins.ZeroFill:
                return Box("Text Zerofill", BoxTypes.Executable, zerofill_text_function(), auto_run=True)

        # Others
        elif builtin_Box_Type in Others:
            if builtin_Box_Type == Others.runOsCommand:
                return Box("Run Os Command", BoxTypes.Executable, runOsCommand_function())
            elif builtin_Box_Type == Others.Eval:
                return Box("Python Eval", BoxTypes.Executable, pythonEval_function())

        # Box Functions
        elif builtin_Box_Type in Boxfunctions:
            if builtin_Box_Type == Boxfunctions.Length:
                return Box("Get Length", BoxTypes.Executable, getLength_function())
            if builtin_Box_Type == Boxfunctions.Sum:
                return Box("Sum", BoxTypes.Executable, sum_function(), addable_left=True)
            if builtin_Box_Type == Boxfunctions.Range:
                return Box("Range", BoxTypes.Executable, range_function())
            if builtin_Box_Type == Boxfunctions.Ord:
                return Box("Ord", BoxTypes.Executable, ord_function())
            if builtin_Box_Type == Boxfunctions.Chr:
                return Box("Chr", BoxTypes.Executable, chr_function())
            if builtin_Box_Type == Boxfunctions.Map:
                return Box("Map", BoxTypes.Executable, map_function())
            if builtin_Box_Type == Boxfunctions.Min:
                return Box("Min", BoxTypes.Executable, min_function(), addable_left=True)
            if builtin_Box_Type == Boxfunctions.Max:
                return Box("Max", BoxTypes.Executable, max_function(), addable_left=True)
            if builtin_Box_Type == Boxfunctions.Exit:
                return Box("Exit", BoxTypes.Executable, exit_function())
            if builtin_Box_Type == Boxfunctions.Zip:
                return Box("Zip", BoxTypes.Executable, zip_function(), addable_left=True)
            if builtin_Box_Type == Boxfunctions.Abs:
                return Box("Abs", BoxTypes.Executable, abs_function())


def make_box_extention(extention_name, box_type, box_name):
    target_box = extentions[extention_name][1][box_type][box_name]
    if target_box[2] and type(target_box[2]) == dict:
        return Box(box_name, target_box[1], target_box[0], **target_box[2])
    else:
        return Box(box_name, target_box[1], target_box[0])
