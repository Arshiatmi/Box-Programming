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
    variable_name = outputs[0].text
    return variables[variable_name]


def getNumberVariable(function_id, inputs, outputs):
    variable_name = outputs[0].text
    return variables[variable_name]


def getTextVariable(function_id, inputs, outputs):
    variable_name = outputs[0].text
    return variables[variable_name]


def setBooleanVariable(function_id, inputs, outputs, value):
    variable_name = inputs[1].text
    variables[variable_name].value = value


def setNumberVariable(function_id, inputs, outputs, value):
    variable_name = inputs[1].text
    variables[variable_name].value = value


def setTextVariable(function_id, inputs, outputs, value):
    variable_name = inputs[1].text
    variables[variable_name].value = value


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
