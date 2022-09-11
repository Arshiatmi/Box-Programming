from loguru import logger

from Utils.enums import AdvancedNumbers, ArrayBuiltins, BoxTypes, Boxfunctions, CastBuiltins, ExecutableBuiltins, FileBuiltins, OperatorBuiltins, Others, TextBuiltins

functions = {}
boxes = {}
options = {}
variables = {}
images = {}
locked_image_objects = []
ALL_GLOBALS = {}

executalbe_categories = [
    ExecutableBuiltins,
    CastBuiltins,
    ArrayBuiltins,
    FileBuiltins,
    TextBuiltins,
    Others,
    AdvancedNumbers,
    Boxfunctions
]

box_categories = {
    BoxTypes.Operator:
        [
            OperatorBuiltins.Add_Two_Numbers,
            OperatorBuiltins.Add_Two_Text,
            OperatorBuiltins.Minus_Two_Numbers,
            OperatorBuiltins.AND,
            OperatorBuiltins.OR,
            OperatorBuiltins.IN,
            OperatorBuiltins.POW,
        ],
    BoxTypes.Executable:
        {
            ExecutableBuiltins:
                [
                    ExecutableBuiltins.If,
                    ExecutableBuiltins.Input,
                    ExecutableBuiltins.Print,
                    ExecutableBuiltins.For,
                ],
            CastBuiltins:
                [
                    CastBuiltins.Number_To_Text,
                    CastBuiltins.Number_To_Bool,
                    CastBuiltins.Bool_To_Number,
                    CastBuiltins.Bool_To_Text,
                    CastBuiltins.Text_To_Number,
                    CastBuiltins.Text_To_Bool,
                    CastBuiltins.Array_To_Text,
                    CastBuiltins.Text_To_Array,
                    CastBuiltins.Variable_To_Text,
                ],
            ArrayBuiltins:
                [
                    ArrayBuiltins.Parse,
                    ArrayBuiltins.Append,
                    ArrayBuiltins.Prepend,
                    ArrayBuiltins.Count,
                    ArrayBuiltins.Index,
                    ArrayBuiltins.Sort,
                    ArrayBuiltins.Insert,
                    ArrayBuiltins.Remove,
                    ArrayBuiltins.MinArray,
                    ArrayBuiltins.MaxArray,
                ],
            FileBuiltins:
                [
                    FileBuiltins.ReadFile,
                    FileBuiltins.WriteFile,
                    FileBuiltins.RemoveFile,
                    FileBuiltins.FileList,
                ],
            TextBuiltins:
                [
                    TextBuiltins.Capitalize,
                    TextBuiltins.Count,
                    TextBuiltins.EndsWith,
                    TextBuiltins.Find,
                    TextBuiltins.IsAlphabet,
                    TextBuiltins.IsAlphabetNumber,
                    TextBuiltins.IsUpperCase,
                    TextBuiltins.IsLowerCase,
                    TextBuiltins.ToUpper,
                    TextBuiltins.ToLower,
                ],
            Others:
                [
                    Others.runOsCommand,
                    Others.Eval
                ],
            AdvancedNumbers:
                [
                    AdvancedNumbers.ToBinary,
                    AdvancedNumbers.FromBinary,
                    AdvancedNumbers.ToOct,
                    AdvancedNumbers.FromOct,
                    AdvancedNumbers.ToHex,
                    AdvancedNumbers.FromHex,
                ],
            Boxfunctions:
                [
                    Boxfunctions.Length,
                    Boxfunctions.Sum,
                    Boxfunctions.Range,
                    Boxfunctions.Ord,
                    Boxfunctions.Chr,
                    Boxfunctions.Map,
                    Boxfunctions.Min,
                    Boxfunctions.Max,
                    Boxfunctions.Exit,
                    Boxfunctions.Zip,
                    Boxfunctions.Abs,
                ],
        }
}
