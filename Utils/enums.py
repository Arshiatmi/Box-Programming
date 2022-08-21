import enum


class Types(enum.Enum):
    boolean = bool
    text = str
    number = float
    empty = 0
    executable = 1


class InputTypes(enum.Enum):
    checkbox = 0
    numberField = 1
    textField = 2
    executeButton = 3


class BoxTypes(enum.Enum):
    Variable = 0
    Executable = 1
    Start = 2
    End = 3

class Sides(enum.Enum):
    left = 0
    right = 1