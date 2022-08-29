from Utils.blocks import Function, Option
from Utils.enums import Types, Sides
from Utils.functions import make_id_from_name
from Utils.helpers import *

add_two_numbers_operator = Function(f"Function Add Two Numbers",
                                    add2vars,
                                    [
                                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n1", Types.number,
                                               Sides.left, indexing=False),
                                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n2", Types.number, Sides.left, indexing=False)],
                                    [
                                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n3", Types.number,
                                               Sides.right, indexing=False)
                                    ])

add_two_text_operator = Function(f"Function Add Two Text",
                                 add2vars,
                                 [
                                     Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n1", Types.text,
                                            Sides.left,indexing=False),
                                     Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n2", Types.text, Sides.left,indexing=False)],
                                 [
                                     Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n3", Types.text,
                                            Sides.right,indexing=False)
                                 ])

minus_two_numbers_operator = Function(f"Function Add Two Number",
                                      minus2Numbers,
                                      [
                                          Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n1", Types.number,
                                                 Sides.left,indexing=False),
                                          Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n2", Types.number, Sides.left,indexing=False)],
                                      [
                                          Option(f"builtin_{make_id_from_name('Function Add Two Number')}_n3", Types.number,
                                                 Sides.right,indexing=False)
                                      ])

AND_operator = Function(f"AND",
                        AND,
                        [
                            Option(f"builtin_{make_id_from_name('AND')}_n1", Types.boolean,
                                   Sides.left,indexing=False),
                            Option(f"builtin_{make_id_from_name('AND')}_n2", Types.boolean, Sides.left,indexing=False)],
                        [
                            Option(f"builtin_{make_id_from_name('AND')}_n3", Types.boolean,
                                   Sides.right,indexing=False)
                        ])

OR_operator = Function(f"OR",
                       OR,
                       [
                           Option(f"builtin_{make_id_from_name('OR')}_n1", Types.boolean,
                                  Sides.left,indexing=False),
                           Option(f"builtin_{make_id_from_name('OR')}_n2", Types.boolean, Sides.left,indexing=False)],
                       [
                           Option(f"builtin_{make_id_from_name('OR')}_n3", Types.boolean,
                                  Sides.right,indexing=False)
                       ])
