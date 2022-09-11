import enum


class customEnum(enum.Enum):
    @classmethod
    def by_value(cls, key):
        attrs = ({j.value: i for i, j in cls.__dict__[
                 '_member_map_'].items()})
        try:
            return getattr(cls, attrs[key])
        except:
            raise
            return None


class Types(customEnum):
    boolean = bool
    text = str
    number = float
    array = list
    empty = 0
    executable = 1
    variable = [bool, str, float, list]


class InputTypes(customEnum):
    checkbox = 0
    numberField = 1
    textField = 2
    executeButton = 3


class BoxTypes(customEnum):
    Variable = 0
    Executable = 1
    Operator = 2
    Event = 3
    Start = 4
    End = 5


class MainBoxTypes(customEnum):
    Builtins = 0
    Extentions = 1


class Sides(customEnum):
    left = 0
    right = 1


class OperatorBuiltins(customEnum):
    Add_Two_Numbers = 1
    Add_Two_Text = 2
    Minus_Two_Numbers = 3
    AND = 4
    OR = 5
    POW = 6
    IN = 7


class ExecutableBuiltins(customEnum):
    If = 1
    Input = 2
    Print = 3
    For = 4


class CastBuiltins(customEnum):
    Number_To_Text = 1
    Number_To_Bool = 2
    Bool_To_Number = 3
    Bool_To_Text = 4
    Text_To_Number = 5
    Text_To_Bool = 6
    Array_To_Text = 7
    Text_To_Array = 8
    Variable_To_Text = 9


class ArrayBuiltins(customEnum):
    Parse = 1
    Append = 2
    Prepend = 3
    Count = 4
    Index = 5
    Insert = 6
    Remove = 7
    Sort = 8
    MinArray = 9
    MaxArray = 10


class FileBuiltins(customEnum):
    ReadFile = 1
    WriteFile = 2
    RemoveFile = 3
    FileList = 4


class TextBuiltins(customEnum):
    Capitalize = 1
    Count = 2
    EndsWith = 3
    Find = 4
    IsAlphabet = 5
    IsAlphabetNumber = 6
    IsDigit = 7
    IsLowerCase = 8
    IsUpperCase = 9
    ToUpper = 10
    ToLower = 11
    Join = 12
    Replace = 13
    Strip = 14
    Split = 15
    SwapCase = 16
    ZeroFill = 17


class Others(customEnum):
    runOsCommand = 1
    Eval = 2


class AdvancedNumbers(customEnum):
    ToBinary = 1
    FromBinary = 2
    ToOct = 3
    FromOct = 4
    ToHex = 5
    FromHex = 6


class Boxfunctions(customEnum):
    Length = 1
    Sum = 2
    Range = 3
    Ord = 4
    Chr = 5
    Map = 6
    Min = 7
    Max = 8
    Exit = 9
    Zip = 10
    Abs = 11
