from .global_vars import *
from .variables import varaibles
from .enums import BoxTypes

def getExecutableFunctions():
    return {i:j for i,j in boxes.items() if j.type == BoxTypes.Executable}

def getVariableFunctions():
    return {i:j for i,j in boxes.items() if j.type == BoxTypes.Variable}

def getAllFunctions():
    o1 = getExecutableFunctions()
    o1.update(getVariableFunctions())
    return o1

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb   

def getBooleanVariable(name):
    return varaibles[name]

def getNumberVariable(name):
    return varaibles[name]

def getTextVariable(name):
    return varaibles[name]

def setBooleanVariable(name,value):
    varaibles[name].value = value

def setNumberVariable(name,value):
    varaibles[name].value = value

def setTextVariable(name,value):
    varaibles[name].value = value