from .global_vars import *
from .variables import variables
from .enums import BoxTypes


def getExecutableFunctions():
    return {i: j for i, j in boxes.items() if j.type == BoxTypes.Executable}


def getVariableFunctions():
    return {i: j for i, j in boxes.items() if j.type == BoxTypes.Variable}


def getOperatorFunctions():
    return {i: j for i, j in boxes.items() if j.type == BoxTypes.Operator}


def getEventFunctions():
    return {i: j for i, j in boxes.items() if j.type == BoxTypes.Event}


def getAllFunctions():
    return boxes


def getBooleanVariable(function_id, inputs, outputs):
    variable_name = outputs[0].variable.id
    return variables[variable_name]


def getNumberVariable(function_id, inputs, outputs):
    variable_name = outputs[0].variable.id
    return variables[variable_name]


def getTextVariable(function_id, inputs, outputs):
    variable_name = outputs[0].variable.id
    return variables[variable_name]


def getArrayVariable(function_id, inputs, outputs):
    variable_name = outputs[0].variable.id
    return variables[variable_name]


def setBooleanVariable(function_id, inputs, outputs, value):
    inputs[1].variable.value = value
    return value


def setNumberVariable(function_id, inputs, outputs, value):
    inputs[1].variable.value = value
    return value


def setTextVariable(function_id, inputs, outputs, value):
    inputs[1].variable.value = value
    return value


def setArrayVariable(function_id, inputs, outputs, value):
    inputs[1].variable.value = value
    return inputs[1].variable


def add2vars(function_id, inputs, outputs):
    first_variable_name = inputs[0].text
    second_variable_name = inputs[1].text
    ans = variables[first_variable_name].value + \
        variables[second_variable_name].value
    outputs[0].value = ans


def minus2Numbers(function_id, inputs, outputs):
    first_variable_name = inputs[0].text
    second_variable_name = inputs[1].text
    ans = variables[first_variable_name].value - \
        variables[second_variable_name].value
    outputs[0].value = ans


def AND(function_id, inputs, outputs):
    first_variable_name = inputs[0].text
    second_variable_name = inputs[1].text
    ans = variables[first_variable_name].value and \
        variables[second_variable_name].value
    outputs[0].value = ans


def OR(function_id, inputs, outputs):
    first_variable_name = inputs[0].text
    second_variable_name = inputs[1].text
    ans = variables[first_variable_name].value or \
        variables[second_variable_name].value
    outputs[0].value = ans


def if_statement(function_id, inputs, outputs):
    if inputs[1].value:
        return outputs[0]
    else:
        return outputs[1]


def get_input(function_id, inputs, outputs):
    outputs[1].value = input(inputs[1].value)
    return outputs[0]


def print_string(function_id, inputs, outputs):
    print(inputs[1].value)
    return outputs[0]


def number_to_text(function_id, inputs, outputs):
    try:
        outputs[2].value = str(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def number_to_bool(function_id, inputs, outputs):
    try:
        outputs[2].value = bool(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def bool_to_number(function_id, inputs, outputs):
    try:
        outputs[2].value = float(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def bool_to_text(function_id, inputs, outputs):
    try:
        outputs[2].value = str(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def text_to_number(function_id, inputs, outputs):
    try:
        outputs[2].value = float(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def text_to_bool(function_id, inputs, outputs):
    try:
        outputs[2].value = bool(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def array_to_text(function_id, inputs, outputs):
    try:
        outputs[2].value = str(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def text_to_array(function_id, inputs, outputs):
    try:
        outputs[2].value = list(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def array_test(function_id, inputs, outputs):
    inputs[0].value.append("test")


def convert_to_list(inputs):
    if not inputs:
        return []
    if type(inputs) == list:
        return inputs
    elif type(inputs) == dict or type(inputs) == tuple or type(inputs) == set or type(inputs) == frozenset:
        ans = []
        for i in inputs:
            ans.append(i.value)
        return ans
    else:
        return [inputs]
