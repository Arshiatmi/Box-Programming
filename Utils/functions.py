from .blocks import Function

def setOptions():
    pass

def getExecutableFunctions():
    return [Function("print",print)]

def getVariableFunctions():
    return []

def getAllFunctions():
    return getVariableFunctions() + getExecutableFunctions()