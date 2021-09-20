import enum

class Types(enum.Enum):
    boolean = bool
    text = str
    number = float
    empty = None
    executable = 1

class InputTypes(enum.Enum):
    checkbox = 0
    numberField = 1
    textField = 2

class BoxTypes(enum.Enum):
    Variable = 0
    Executable = 1
    Start = 2
    End = 3

class ConfigModes(enum.Enum):
    line_mode = 0
    box_mode = 1
    normal = 2