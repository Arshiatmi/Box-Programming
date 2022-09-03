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
                               Types.text, Sides.left, optional=True)
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
