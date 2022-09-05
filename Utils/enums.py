import enum


class Types(enum.Enum):
    boolean = bool
    text = str
    number = float
    array = list
    empty = 0
    executable = 1
    variable = [bool, str, float, list]


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
    Input = 2
    Print = 3
    For = 4


class CastBuiltins(enum.Enum):
    Number_To_Text = 1
    Number_To_Bool = 2
    Bool_To_Number = 3
    Bool_To_Text = 4
    Text_To_Number = 5
    Text_To_Bool = 6
    Array_To_Text = 7
    Text_To_Array = 8
    Variable_To_Text = 9


class ArrayBuiltins(enum.Enum):
    Parse = 1
    Append = 2
    Clear = 3
    Count = 4
    Index = 5
    Insert = 6
    Remove = 7
    Sort = 7


class FileBuiltins(enum.Enum):
    ReadFile = 1
    WriteFile = 2
    RemoveFile = 3
    FileList = 4


class TextBuiltins(enum.Enum):
    Capitalize = 1
    Count = 2
    EndsWith = 3
    Find = 4
    Index = 5
    IsAlphabet = 6
    IsAlphabetNumber = 7
    IsDigit = 8
    IsLowerCase = 9
    IsUpperCase = 10
    Join = 11
    Replace = 12
    rFind = 13
    Strip = 14
    rStrip = 15
    Split = 16
    SwapCase = 17
    ZeroFill = 18
