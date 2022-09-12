import eel
from Utils.extention_manager import *
from Utils.builtins import define_variable, make_box, make_box_extention
from Utils.variables import *
from Utils.blocks import *
from Utils.helpers import *


@eel.expose
def make_box_connector(box_type, first_index, second_index=None, from_extention=False, extention_name=None):
    box = None
    if box_type == 1:
        if second_index is None:
            logger.error(
                "For Executable Type Boxes, second_index Should Be Setted.")
        tp = BoxTypes.Executable
        if from_extention:
            if not extention_name:
                logger.error(
                    "For Extention Type Boxes, extention_name Should Be Setted.")
            if type(first_index) != str:
                logger.error(
                    "For Extention Type Boxes, first_index Should Be Box Name.")
            box_exact = extentions[extention_name][1][box_type][first_index]
            box = make_box_extention(first_index, tp,
                                     box_exact)
        else:
            box_exact = box_categories[tp][MainBoxTypes.Builtins][executalbe_categories[first_index]][second_index]
            box = make_box(box_exact,
                           tp)
    elif box_type == 2:
        tp = BoxTypes.Operator
        if from_extention:
            if not extention_name:
                logger.error(
                    "For Extention Type Boxes, extention_name Should Be Setted.")
            box_exact = extentions[extention_name][1][box_type][first_index]
            box = make_box_extention(first_index, tp,
                                     box_exact)
        else:
            box_exact = box_categories[tp][MainBoxTypes.Builtins][first_index]
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
def detach_connector(box_id, box_to_detach, self_index, target_option_or_value, side=Sides.left.value):
    if not box_to_attach:
        box_to_attach = None
    side = Sides.by_value(side)
    boxes[box_id].detach(box_to_detach, self_index,
                         target_option_or_value, side)


@eel.expose
def execute_box_connector(box_id):
    next_box = boxes[box_id].execute_box()
    return next_box.id


@eel.expose
def outputs_connector(box_id):
    ans = {i.id: i.value for i in boxes[box_id].outputs}
    return ans


@eel.expose
def inputs_connector(box_id):
    ans = {i.id: i.value for i in boxes[box_id].inputs}
    return ans


@eel.expose
def set_option_text(option_id, text):
    try:
        options[option_id].text = text
        return True
    except:
        return False


@eel.expose
def define_variable_connector(name, Type):
    if Type == 1:
        Type = Types.boolean
    elif Type == 2:
        Type = Types.text
    elif Type == 3:
        Type = Types.number
    elif Type == 4:
        Type = Types.array
    elif Type == 5:
        Type = Types.empty
    elif Type == 7:
        Type = Types.variable
    get_variable, set_variable = define_variable(name, Type)
    return {"get": get_variable.id, "set": set_variable.id}


@eel.expose
def get_variable(var_id):
    try:
        return variables[var_id]
    except:
        return None


@eel.expose
def run_box(box_id, *arguments):
    target_box = boxes[box_id]
    if arguments:
        return target_box(*arguments)
    else:
        return target_box()


@eel.expose
def set_variable(var_id, data):
    try:
        variables[var_id]
        variables[var_id] = data
    except:
        logger.error(f"Variable {var_id} Is Not Defined :(")


@eel.expose
def box_details_connector(box_id):
    box: Box = boxes[box_id]
    ans = {
        "id": box_id,
        "name": box.name,
        "inputs": {i.id: i.value for i in box.inputs},
        "outputs": {i.id: i.value for i in box.outputs},
        "auto_run": box.auto_run,
        "addable_left": box.addable_left,
        "addable_right": box.addable_right,
        "type": box.Type,
    }
    return ans
