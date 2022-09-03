from Utils.blocks import Function, Option
from Utils.enums import Types, Sides
from Utils.functions import make_id_from_name
from Utils.helpers import *

add_two_numbers_operator = Function(f"Function Add Two Numbers",
                                    add2vars,
                                    [
                                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n1", Types.number,
                                               Sides.left),
                                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n2", Types.number, Sides.left)],
                                    [
                                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n3", Types.number,
                                               Sides.right)
                                    ])

add_two_text_operator = Function(f"Function Add Two Text",
                                 add2vars,
                                 [
                                     Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n1", Types.text,
                                            Sides.left),
                                     Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n2", Types.text, Sides.left)],
                                 [
                                     Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n3", Types.text,
                                            Sides.right)
                                 ])

minus_two_numbers_operator = Function(f"Function Add Two Number",
                                      minus2Numbers,
                                      [
                                          Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n1", Types.number,
                                                 Sides.left),
                                          Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n2", Types.number, Sides.left)],
                                      [
                                          Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n3", Types.number,
                                                 Sides.right)
                                      ])

AND_operator = Function(f"AND",
                        AND,
                        [
                            Option(f"builtin_{make_id_from_name('AND')}_n1", Types.boolean,
                                   Sides.left),
                            Option(f"builtin_{make_id_from_name('AND')}_n2", Types.boolean, Sides.left)],
                        [
                            Option(f"builtin_{make_id_from_name('AND')}_n3", Types.boolean,
                                   Sides.right)
                        ])

OR_operator = Function(f"OR",
                       OR,
                       [
                           Option(f"builtin_{make_id_from_name('OR')}_n1", Types.boolean,
                                  Sides.left),
                           Option(f"builtin_{make_id_from_name('OR')}_n2", Types.boolean, Sides.left)],
                       [
                           Option(f"builtin_{make_id_from_name('OR')}_n3", Types.boolean,
                                  Sides.right)
                       ])

if_statement_function = Function("If",
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
                                 ])

get_input_function = Function("Input",
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
                              ])
