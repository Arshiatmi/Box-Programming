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


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def getBooleanVariable(name, inputs, outputs):
    variable_name = functions[name].outputs[0].text
    return variables[variable_name]


def getNumberVariable(name, inputs, outputs):
    variable_name = functions[name].outputs[0].text
    return variables[variable_name]


def getTextVariable(name, inputs, outputs):
    variable_name = functions[name].outputs[0].text
    return variables[variable_name]


def setBooleanVariable(name, inputs, outputs, value):
    variable_name = functions[name].inputs[1].text
    variables[variable_name].value = value


def setNumberVariable(name, inputs, outputs, value):
    variable_name = functions[name].inputs[1].text
    variables[variable_name].value = value


def setTextVariable(name, inputs, outputs, value):
    variable_name = functions[name].inputs[1].text
    variables[variable_name].value = value


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
