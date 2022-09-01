import enum


class Types(enum.Enum):
    boolean = bool
    text = str
    number = float
    array = list
    empty = 0
    executable = 1
    variable = 2


class InputTypes(enum.Enum):
    checkbox = 0
    numberField = 1
    textField = 2
    executeButton = 3


class BoxTypes(enum.Enum):
    Variable = 0
    Executable = 1
    Operator = 2
    Event = 3
    Start = 4
    End = 5


class Sides(enum.Enum):
    left = 0
    right = 1


class OperatorBuiltins(enum.Enum):
    Add_Two_Numbers = 1
    Add_Two_Text = 2
    Minus_Two_Numbers = 3
    AND = 4
    OR = 5


class ExecutableBuiltins(enum.Enum):
    If = 1
