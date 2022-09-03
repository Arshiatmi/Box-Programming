from Utils.blocks import Function, Option
from Utils.enums import Types, Sides
from Utils.functions import make_id_from_name
from Utils.helpers import *


def add_two_numbers_operator():
    return Function(f"Function Add Two Numbers",
                    add2vars,
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n1", Types.number,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n2", Types.number, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n3", Types.number,
                               Sides.right)
                    ], is_instance=True)


def add_two_text_operator():
    return Function(f"Function Add Two Text",
                    add2vars,
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n1", Types.text,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n2", Types.text, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n3", Types.text,
                               Sides.right)
                    ], is_instance=True)


def minus_two_numbers_operator():
    return Function(f"Function Add Two Number",
                    minus2Numbers,
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n1", Types.number,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n2", Types.number, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n3", Types.number,
                               Sides.right)
                    ], is_instance=True)


def AND_operator():
    return Function(f"AND",
                    AND,
                    [
                        Option(f"builtin_{make_id_from_name('AND')}_n1", Types.boolean,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('AND')}_n2", Types.boolean, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('AND')}_n3", Types.boolean,
                               Sides.right)
                    ], is_instance=True)


def OR_operator():
    return Function(f"OR",
                    OR,
                    [
                        Option(f"builtin_{make_id_from_name('OR')}_n1", Types.boolean,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('OR')}_n2", Types.boolean, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('OR')}_n3", Types.boolean,
                               Sides.right)
                    ], is_instance=True)


def if_statement_function():
    return Function("If",
                    if_statement,
                    [
                        Option("builtin_If",
                               Types.executable, Sides.left),
                        Option("builtin_If_bool", Types.boolean, Sides.left)],
                    [
                        Option("True", Types.executable,
                               Sides.right, show_text=True),
                        Option("False", Types.executable,
                               Sides.right, show_text=True)
                    ], is_instance=True)


def get_input_function():
    return Function("Input",
                    get_input,
                    [
                        Option("builtin_Input",
                               Types.executable, Sides.left),
                        Option("builtin_Input_prompt", Types.text, Sides.left)],
                    [
                        Option("builtin_Input",
                               Types.executable, Sides.right),
                        Option("builtin_Input_text",
                               Types.text, Sides.right, optional=True)
                    ], is_instance=True)


def print_string_function():
    return Function("Print",
                    print_string,
                    [
                        Option("builtin_Print",
                               Types.executable, Sides.left),
                        Option("builtin_Print_String", Types.text, Sides.left)],
                    [
                        Option("builtin_Print",
                               Types.executable, Sides.right),
                    ], is_instance=True)


def number_to_text_function():
    return Function("Number To Text",
                    number_to_text,
                    [
                        Option("builtin_Cast_NumberToText",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_NumberToText_input", Types.number, Sides.left)],
                    [
                        Option("builtin_Cast_NumberToText",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_NumberToText_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_NumberToText_output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def number_to_bool_function():
    return Function("Number To Bool",
                    number_to_bool,
                    [
                        Option("builtin_Cast_NumberToBool",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_NumberToBool_input", Types.number, Sides.left)],
                    [
                        Option("builtin_Cast_NumberToBool",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_NumberToBool_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_NumberToBool_output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def bool_to_number_function():
    return Function("Bool To Number",
                    bool_to_number,
                    [
                        Option("builtin_Cast_BoolToNumber",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_BoolToNumber_input", Types.boolean, Sides.left)],
                    [
                        Option("builtin_Cast_BoolToNumber",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_BoolToNumber_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_BoolToNumber_output",
                               Types.number, Sides.right),
                    ], is_instance=True)


def bool_to_text_function():
    return Function("Bool To Text",
                    bool_to_text,
                    [
                        Option("builtin_Cast_BoolToText",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_BoolToText_input", Types.boolean, Sides.left)],
                    [
                        Option("builtin_Cast_BoolToText",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_BoolToText_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_BoolToText_output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def text_to_number_function():
    return Function("Text To Number",
                    text_to_number,
                    [
                        Option("builtin_Cast_TextToNumber",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_TextToNumber_input", Types.text, Sides.left)],
                    [
                        Option("builtin_Cast_TextToNumber",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToNumber_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToNumber_output",
                               Types.number, Sides.right),
                    ], is_instance=True)


def text_to_bool_function():
    return Function("Text To Bool",
                    text_to_bool,
                    [
                        Option("builtin_Cast_TextToBool",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_TextToBool_input", Types.text, Sides.left)],
                    [
                        Option("builtin_Cast_TextToBool",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToBool_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToBool_output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def array_to_text_function():
    return Function("Array To Text",
                    array_to_text,
                    [
                        Option("builtin_Cast_ArrayToText",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_ArrayToText_input", Types.array, Sides.left)],
                    [
                        Option("builtin_Cast_ArrayToText",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_ArrayToText_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_ArrayToText_output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def text_to_array_function():
    return Function("Text To Array",
                    text_to_array,
                    [
                        Option("builtin_Cast_TextToArray",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_TextToArray_input", Types.text, Sides.left)],
                    [
                        Option("builtin_Cast_TextToArray",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToArray_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToArray_output",
                               Types.array, Sides.right),
                    ], is_instance=True)
