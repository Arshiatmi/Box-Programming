import enum

class Types(enum.Enum):
    boolean = bool
    string = str
    number = float

class InputTypes(enum.Enum):
    checkbox = 0
    numberField = 1
    textField = 2

class BoxTypes(enum.Enum):
    Variable = 0
    Executable = 1