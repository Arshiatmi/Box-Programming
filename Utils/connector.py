import eel
from Utils.extention_manager import *
from Utils.builtins import define_variable, make_box
from Utils.variables import *
from Utils.blocks import *
from Utils.helpers import *


@eel.expose
def make_box_connector(box_type, first_index, second_index=None):
    box = None
    if box_type == 1:
        if second_index is None:
            logger.error(
                "For Executable Type Boxes, second_index Should Be Setted.")
        tp = BoxTypes.Executable
        box_exact = box_categories[tp][executalbe_categories[first_index]][second_index]
        box = make_box(box_exact,
                       tp)
    elif box_type == 2:
        tp = BoxTypes.Operator
        box_exact = box_categories[tp][first_index]
        box = make_box(box_exact,
                       tp)
    return box.id


@eel.expose
def attach_connector(box_id, box_to_attach, self_index, target_option_or_value, side=Sides.left.value):
    if not box_to_attach:
        box_to_attach = None
    side = Sides.by_value(side)
    boxes[box_id].attach(box_to_attach, self_index,
                         target_option_or_value, side)


@eel.expose
def execute_box_connector(box_id, box_to_attach, self_index, target_option_or_value, side=Sides.left.value):
    next_box = boxes[box_id].execute_box()
    return next_box.id


@eel.expose
def outputs_connector(box_id):
    ans = [i.value for i in boxes[box_id].outputs]
    return ans
