from Utils.blocks import Function, Option
from Utils.enums import Types, Sides
from Utils.functions import make_id_from_name
from Utils.helpers import *


def add_two_numbers_operator():
    return Function(f"Add Two Numbers Function",
                    add2vars,
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n1", Types.number,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n2", Types.number, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Numbers')}_n3", Types.number,
                               Sides.right)
                    ], is_instance=True)


def add_two_text_operator():
    return Function(f"Add Two Text Function",
                    add2vars,
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n1", Types.text,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n2", Types.text, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('Function Add Two Text')}_n3", Types.text,
                               Sides.right)
                    ], is_instance=True)


def minus_two_numbers_operator():
    return Function(f"Minus Two Numbers Function",
                    minus2Numbers,
                    [
                        Option(f"builtin_{make_id_from_name('Function Minus Two Numbers')}_n1", Types.number,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('Function Minus Two Numbers')}_n2", Types.number, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('Function Minus Two Numbers')}_n3", Types.number,
                               Sides.right)
                    ], is_instance=True)


def AND_operator():
    return Function(f"AND Function",
                    AND,
                    [
                        Option(f"builtin_{make_id_from_name('AND')}_n1", Types.boolean,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('AND')}_n2", Types.boolean, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('AND')}_n3", Types.boolean,
                               Sides.right)
                    ], is_instance=True)


def OR_operator():
    return Function(f"OR Function",
                    OR,
                    [
                        Option(f"builtin_{make_id_from_name('OR')}_n1", Types.boolean,
                               Sides.left),
                        Option(f"builtin_{make_id_from_name('OR')}_n2", Types.boolean, Sides.left)],
                    [
                        Option(f"builtin_{make_id_from_name('OR')}_n3", Types.boolean,
                               Sides.right)
                    ], is_instance=True)


def if_statement_function():
    return Function("If Function",
                    if_statement,
                    [
                        Option("builtin_If",
                               Types.executable, Sides.left),
                        Option("builtin_If_bool", Types.boolean, Sides.left)],
                    [
                        Option("True", Types.executable,
                               Sides.right, show_text=True),
                        Option("False", Types.executable,
                               Sides.right, show_text=True)
                    ], is_instance=True)


def get_input_function():
    return Function("Input Function",
                    get_input,
                    [
                        Option("builtin_Input",
                               Types.executable, Sides.left),
                        Option("builtin_Input_prompt", Types.text, Sides.left)],
                    [
                        Option("builtin_Input",
                               Types.executable, Sides.right),
                        Option("builtin_Input_text",
                               Types.text, Sides.right, optional=True)
                    ], is_instance=True)


def print_string_function():
    return Function("Print Function",
                    print_string,
                    [
                        Option("builtin_Print",
                               Types.executable, Sides.left),
                        Option("builtin_Print_String", Types.text, Sides.left)],
                    [
                        Option("builtin_Print",
                               Types.executable, Sides.right),
                    ], is_instance=True)


def number_to_text_function():
    return Function("Number To Text Function",
                    number_to_text,
                    [
                        Option("builtin_Cast_NumberToText",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_NumberToText_input", Types.number, Sides.left)],
                    [
                        Option("builtin_Cast_NumberToText",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_NumberToText_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_NumberToText_output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def number_to_bool_function():
    return Function("Number To Bool Function",
                    number_to_bool,
                    [
                        Option("builtin_Cast_NumberToBool",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_NumberToBool_input", Types.number, Sides.left)],
                    [
                        Option("builtin_Cast_NumberToBool",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_NumberToBool_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_NumberToBool_output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def bool_to_number_function():
    return Function("Bool To Number Function",
                    bool_to_number,
                    [
                        Option("builtin_Cast_BoolToNumber",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_BoolToNumber_input", Types.boolean, Sides.left)],
                    [
                        Option("builtin_Cast_BoolToNumber",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_BoolToNumber_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_BoolToNumber_output",
                               Types.number, Sides.right),
                    ], is_instance=True)


def bool_to_text_function():
    return Function("Bool To Text Function",
                    bool_to_text,
                    [
                        Option("builtin_Cast_BoolToText",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_BoolToText_input", Types.boolean, Sides.left)],
                    [
                        Option("builtin_Cast_BoolToText",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_BoolToText_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_BoolToText_output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def text_to_number_function():
    return Function("Text To Number Function",
                    text_to_number,
                    [
                        Option("builtin_Cast_TextToNumber",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_TextToNumber_input", Types.text, Sides.left)],
                    [
                        Option("builtin_Cast_TextToNumber",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToNumber_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToNumber_output",
                               Types.number, Sides.right),
                    ], is_instance=True)


def text_to_bool_function():
    return Function("Text To Bool Function",
                    text_to_bool,
                    [
                        Option("builtin_Cast_TextToBool",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_TextToBool_input", Types.text, Sides.left)],
                    [
                        Option("builtin_Cast_TextToBool",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToBool_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToBool_output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def array_to_text_function():
    return Function("Array To Text Function",
                    array_to_text,
                    [
                        Option("builtin_Cast_ArrayToText",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_ArrayToText_input", Types.array, Sides.left)],
                    [
                        Option("builtin_Cast_ArrayToText",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_ArrayToText_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_ArrayToText_output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def text_to_array_function():
    return Function("Text To Array Function",
                    text_to_array,
                    [
                        Option("builtin_Cast_TextToArray",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_TextToArray_input", Types.text, Sides.left)],
                    [
                        Option("builtin_Cast_TextToArray",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToArray_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_TextToArray_output",
                               Types.array, Sides.right),
                    ], is_instance=True)


def variable_to_text_function():
    return Function("Variable To Text Function",
                    variable_to_text,
                    [
                        Option("builtin_Cast_VariableToText",
                               Types.executable, Sides.left),
                        Option("builtin_Cast_VariableToText_input", Types.variable, Sides.left)],
                    [
                        Option("builtin_Cast_VariableToText",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_VariableToText_failed",
                               Types.executable, Sides.right),
                        Option("builtin_Cast_VariableToText_output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def parse_array_function():
    return Function("Parse Array Function",
                    parse_array,
                    [
                        Option("builtin_Array_Parse_Input",
                               Types.array, Sides.left),
                    ],
                    [
                        Option("builtin_Array_Parse_Length",
                               Types.number, Sides.right),
                        Option("builtin_Array_Parse_Elements",
                               Types.array, Sides.right),
                        Option("builtin_Array_Parse_Reversed",
                               Types.array, Sides.right),
                    ], is_instance=True)


def append_array_function():
    return Function("Append To Array Function",
                    append_array,
                    [
                        Option("builtin_Array_Append_Input",
                               Types.array, Sides.left),
                        Option("builtin_Array_Append_Element",
                               Types.variable, Sides.left),
                    ],
                    [
                        Option("builtin_Array_Append_Output",
                               Types.array, Sides.right),
                    ], is_instance=True)


def prepend_array_function():
    return Function("Prepend To Array Function",
                    prepend_array,
                    [
                        Option("builtin_Array_Prepend_Input",
                               Types.array, Sides.left),
                        Option("builtin_Array_Prepend_Element",
                               Types.variable, Sides.left),
                    ],
                    [
                        Option("builtin_Array_Prepend_Output",
                               Types.array, Sides.right),
                    ], is_instance=True)


def sort_array_function():
    return Function("Sort Array Function",
                    sort_array,
                    [
                        Option("builtin_Array_Sort_Input",
                               Types.array, Sides.left),
                    ],
                    [
                        Option("builtin_Array_Prepend_Output",
                               Types.array, Sides.right),
                    ], is_instance=True)


def count_elements_array_function():
    return Function("Count Elements In Array Function",
                    count_elements_array,
                    [
                        Option("builtin_Array_Count_Input",
                               Types.array, Sides.left),
                        Option("builtin_Array_Count_Element",
                               Types.variable, Sides.left),
                    ],
                    [
                        Option("builtin_Array_Count_Output",
                               Types.number, Sides.right),
                    ], is_instance=True)


def index_element_array_function():
    return Function("Index Of Element In Array Function",
                    index_element_array,
                    [
                        Option("builtin_Array_Index_Input",
                               Types.array, Sides.left),
                        Option("builtin_Array_Index_Element",
                               Types.variable, Sides.left),
                    ],
                    [
                        Option("builtin_Array_Index_Output",
                               Types.number, Sides.right),
                    ], is_instance=True)


def insert_element_array_function():
    return Function("Insert Element In Array Function",
                    insert_element_array,
                    [
                        Option("builtin_Array_Insert_Input",
                               Types.array, Sides.left),
                        Option("builtin_Array_Insert_Element",
                               Types.variable, Sides.left),
                        Option("builtin_Array_Insert_Index",
                               Types.number, Sides.left),
                    ],
                    [
                        Option("builtin_Array_Insert_Output",
                               Types.array, Sides.right),
                        Option("builtin_Array_Insert_Success",
                               Types.boolean, Sides.right, default=True),
                    ], is_instance=True)


def remove_element_array_function():
    return Function("Remove Element From Array Function",
                    remove_element_array,
                    [
                        Option("builtin_Array_Remove_Input",
                               Types.array, Sides.left),
                        Option("builtin_Array_Remove_Element",
                               Types.variable, Sides.left),
                        Option("builtin_Array_Should_Remove_Index",
                               Types.boolean, Sides.left, default=False),
                    ],
                    [
                        Option("builtin_Array_Remove_Output",
                               Types.array, Sides.right),
                        Option("builtin_Array_Remove_Success",
                               Types.boolean, Sides.right, default=True),
                    ], is_instance=True)


def for_loop_function():
    return Function("For Loop Function",
                    for_loop,
                    [
                        Option("builtin_For_Loop",
                               Types.executable, Sides.left),
                        Option("builtin_For_Loop_Start",
                               Types.number, Sides.left, default=0),
                        Option("builtin_For_Loop_End",
                               Types.number, Sides.left, default=10),
                        Option("builtin_For_Loop_Step",
                               Types.number, Sides.left, default=1),
                        Option("builtin_For_Loop_Array",
                               Types.array, Sides.left, default=[]),
                    ],
                    [
                        Option("builtin_For_Loop_Finished",
                               Types.executable, Sides.right),
                        Option("builtin_For_Loop",
                               Types.executable, Sides.right),
                        Option("builtin_For_Loop_Index",
                               Types.number, Sides.right),
                        Option("builtin_For_Loop_Element",
                               Types.variable, Sides.right),
                    ], is_instance=True)


def runOsCommand_function():
    return Function("Run Os Command Function",
                    runOsCommand,
                    [
                        Option("builtin_Run_Os_Command",
                               Types.executable, Sides.left),
                        Option("builtin_Run_Os_Command_Text",
                               Types.text, Sides.left),
                        Option("builtin_Run_Os_Command_AsProcess",
                               Types.boolean, Sides.left, default=True),
                    ],
                    [
                        Option("builtin_Run_Os_Command",
                               Types.executable, Sides.right),
                        Option("builtin_Run_Os_Command_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def pythonEval_function():
    return Function("Python Evaluate Function",
                    pythonEvaluate,
                    [
                        Option("builtin_Python_Evaluate",
                               Types.executable, Sides.left),
                        Option("builtin_Python_Evaluate_Text",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Python_Evaluate",
                               Types.executable, Sides.right),
                        Option("builtin_Python_Evaluate_Output",
                               Types.text, Sides.right),
                        Option("builtin_Python_Evaluate_Success",
                               Types.boolean, Sides.right, default=True),
                    ], is_instance=True)

############################################################################################
#                                        File                                              #


def read_file_function():
    return Function("Read File Function",
                    read_file,
                    [
                        Option("builtin_ReadFile",
                               Types.executable, Sides.left),
                        Option("builtin_ReadFile_Name",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_ReadFile",
                               Types.executable, Sides.right),
                        Option("builtin_ReadFile_Data",
                               Types.text, Sides.right),
                        Option("builtin_ReadFile_Data_List",
                               Types.array, Sides.right),
                    ], is_instance=True)


def write_file_function():
    return Function("Write File Function",
                    write_file,
                    [
                        Option("builtin_WriteFile",
                               Types.executable, Sides.left),
                        Option("builtin_WriteFile_Name",
                               Types.text, Sides.left),
                        Option("builtin_WriteFile_Text",
                               Types.text, Sides.left),
                        Option("builtin_WriteFile_ShouldAppend",
                               Types.boolean, Sides.left, default=True),
                    ],
                    [
                        Option("builtin_WriteFile",
                               Types.executable, Sides.right),
                        Option("builtin_WriteFile_Success",
                               Types.boolean, Sides.right, default=True),
                    ], is_instance=True)


def delete_file_function():
    return Function("Delete File Function",
                    delete_file,
                    [
                        Option("builtin_DeleteFile",
                               Types.executable, Sides.left),
                        Option("builtin_DeleteFile_Name",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_DeleteFile",
                               Types.executable, Sides.right),
                        Option("builtin_DeleteFile_Success",
                               Types.boolean, Sides.right, default=True),
                    ], is_instance=True)


def file_list_function():
    return Function("Delete File Function",
                    file_list,
                    [
                        Option("builtin_FileList",
                               Types.executable, Sides.left),
                        Option("builtin_FileList_Path",
                               Types.text, Sides.left, default='.'),
                        Option("builtin_FileList_Contain_Files",
                               Types.boolean, Sides.left, default=True),
                        Option("builtin_FileList_Contain_Directories",
                               Types.boolean, Sides.left, default=True),
                    ],
                    [
                        Option("builtin_FileList",
                               Types.executable, Sides.right),
                        Option("builtin_FileList_Files",
                               Types.array, Sides.right),
                        Option("builtin_FileList_Success",
                               Types.boolean, Sides.right, default=True),
                    ], is_instance=True)

#                                        File                                              #
############################################################################################

# -----------------------------------------------------------------------------------------------------

############################################################################################
#                                        Text                                              #


def capitalize_text_function():
    return Function("Capitalize Text Function",
                    capitalize_text,
                    [
                        Option("builtin_Text_Capitalize_Input",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Capitalize_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def find_text_function():
    return Function("Find Text Function",
                    find_text,
                    [
                        Option("builtin_Text_Find_Input",
                               Types.text, Sides.left),
                        Option("builtin_Text_Find_Element_To_Search",
                               Types.text, Sides.left),
                        Option("builtin_Text_Find_Reverse_Search",
                               Types.boolean, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Find_Output",
                               Types.number, Sides.right),
                    ], is_instance=True)


def join_text_function():
    return Function("Join Text Function",
                    join_text,
                    [
                        Option("builtin_Text_Join_Text",
                               Types.text, Sides.left),
                        Option("builtin_Text_Join_Array",
                               Types.array, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Join_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def replace_text_function():
    return Function("Replace Text Function",
                    replace_text,
                    [
                        Option("builtin_Text_Replace_Text",
                               Types.text, Sides.left),
                        Option("builtin_Text_Replace_Search_Text",
                               Types.text, Sides.left),
                        Option("builtin_Text_Replace_To_Replace",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Replace_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def strip_text_function():
    return Function("Strip Text Function",
                    strip_text,
                    [
                        Option("builtin_Text_Strip_Text",
                               Types.text, Sides.left),
                        Option("builtin_Text_Strip_Chars_To_Remove",
                               Types.text, Sides.left),
                        Option("builtin_Text_Strip_Left",
                               Types.boolean, Sides.left, default=True),
                        Option("builtin_Text_Strip_Right",
                               Types.boolean, Sides.left, default=True),
                    ],
                    [
                        Option("builtin_Text_Strip_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def split_text_function():
    return Function("Split Text Function",
                    split_text,
                    [
                        Option("builtin_Text_Split_Text",
                               Types.text, Sides.left),
                        Option("builtin_Text_Split_Splitter",
                               Types.text, Sides.left),
                        Option("builtin_Text_Split_Max_Split_Count",
                               Types.number, Sides.left),
                        Option("builtin_Text_Split_Start_Index",
                               Types.number, Sides.left),
                        Option("builtin_Text_Split_End_Index",
                               Types.number, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Split_Output",
                               Types.array, Sides.right),
                    ], is_instance=True)


def swapcase_text_function():
    return Function("Swapcase Text Function",
                    swapcase_text,
                    [
                        Option("builtin_Text_Swapcase_Text",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Swapcase_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def zerofill_text_function():
    return Function("ZeroFill Text Function",
                    zerofill_text,
                    [
                        Option("builtin_Text_Zerofill_Text",
                               Types.text, Sides.left),
                        Option("builtin_Text_Zerofill_Zero_Count",
                               Types.number, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Zerofill_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def isalphabet_function():
    return Function("Is Alphabet Text Function",
                    isalphabet_text,
                    [
                        Option("builtin_Text_IsAlphabet_Input",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_IsAlphabet_Output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def isalphabetnumber_function():
    return Function("Is Alphabet Or Number Or Both Text Function",
                    isalphabetnumber_text,
                    [
                        Option("builtin_Text_IsAlphabetOrNumber_Input",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_IsAlphabetOrNumber_Output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def isdigits_function():
    return Function("Is Digit Text Function",
                    isdigit_text,
                    [
                        Option("builtin_Text_IsDigits_Input",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_IsDigits_Output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def islower_function():
    return Function("Is Lower Text Function",
                    islowercase_text,
                    [
                        Option("builtin_Text_IsLower_Input",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_IsLower_Output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def isupper_function():
    return Function("Is Upper Text Function",
                    isuppercase_text,
                    [
                        Option("builtin_Text_IsUpper_Input",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_IsUpper_Output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def toupper_function():
    return Function("To Upper Text Function",
                    touppercase_text,
                    [
                        Option("builtin_Text_ToUpper_Input",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_ToUpper_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def tolower_function():
    return Function("To Lower Text Function",
                    tolowercase_text,
                    [
                        Option("builtin_Text_ToLower_Input",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_ToLower_Output",
                               Types.text, Sides.right),
                    ], is_instance=True)


def count_text_function():
    return Function("Capitalize Text Function",
                    count_text,
                    [
                        Option("builtin_Text_Count_Input",
                               Types.text, Sides.left),
                        Option("builtin_Text_Count_Element_To_search",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Count_Output",
                               Types.number, Sides.right),
                    ], is_instance=True)


def endswith_text_function():
    return Function("Endswith Text Function",
                    endswith_text,
                    [
                        Option("builtin_Text_Endswith_Input",
                               Types.text, Sides.left),
                        Option("builtin_Text_Endswith_Element_To_search",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Text_Endswith_Output",
                               Types.boolean, Sides.right),
                    ], is_instance=True)

#                                        Text                                              #
############################################################################################


############################################################################################
#                                    Box Functions                                         #

def getLength_function():
    return Function("Get Length Function",
                    get_length,
                    [
                        Option("builtin_GetLength",
                               Types.executable, Sides.left),
                        Option("builtin_GetLength_Object",
                               Types.variable, Sides.left),
                    ],
                    [
                        Option("builtin_GetLength",
                               Types.executable, Sides.right),
                        Option("builtin_GetLength_Output",
                               Types.number, Sides.right),
                        Option("builtin_GetLength_Success",
                               Types.boolean, Sides.right, default=True),
                    ], is_instance=True)


def sum_function():
    return Function("Sum Function",
                    sum_of_data,
                    [
                        Option("builtin_Sum",
                               Types.executable, Sides.left),
                        Option("builtin_Sum_Object",
                               Types.variable, Sides.left),
                    ],
                    [
                        Option("builtin_Sum",
                               Types.executable, Sides.right),
                        Option("builtin_GetLength_Output",
                               Types.number, Sides.right),
                        Option("builtin_GetLength_Success",
                               Types.boolean, Sides.right, default=True),
                    ], is_instance=True)


def range_function():
    return Function("Range Function",
                    Range,
                    [
                        Option("builtin_Range",
                               Types.executable, Sides.left),
                        Option("builtin_Range_Start_Index",
                               Types.number, Sides.left),
                        Option("builtin_Range_End_Index",
                               Types.number, Sides.left),
                        Option("builtin_Range_Step_Index",
                               Types.number, Sides.left, default=1),
                    ],
                    [
                        Option("builtin_Range",
                               Types.executable, Sides.right),
                        Option("builtin_Range_Output",
                               Types.array, Sides.right),
                    ], is_instance=True)


def ord_function():
    return Function("Ord Function",
                    Ord,
                    [
                        Option("builtin_Ord",
                               Types.executable, Sides.left),
                        Option("builtin_Ord_Text",
                               Types.text, Sides.left),
                    ],
                    [
                        Option("builtin_Ord",
                               Types.executable, Sides.right),
                        Option("builtin_Ord_Output",
                               Types.array, Sides.right),
                        Option("builtin_Ord_Success",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def chr_function():
    return Function("Chr Function",
                    Chr,
                    [
                        Option("builtin_Chr",
                               Types.executable, Sides.left),
                        Option("builtin_Chr_Characters",
                               Types.array, Sides.left),
                        Option("builtin_Chr_AsText",
                               Types.boolean, Sides.left),
                    ],
                    [
                        Option("builtin_Chr",
                               Types.executable, Sides.right),
                        Option("builtin_Chr_Output",
                               Types.variable, Sides.right),
                        Option("builtin_Chr_Success",
                               Types.boolean, Sides.right),
                    ], is_instance=True)


def map_function():
    return Function("Map Function",
                    Map,
                    [
                        Option("builtin_Map",
                               Types.executable, Sides.left),
                        Option("builtin_Map_Array",
                               Types.array, Sides.left),
                    ],
                    [
                        Option("builtin_Map",
                               Types.executable, Sides.right),
                        Option("builtin_Map_Functionallity",
                               Types.executable, Sides.right),
                        Option("builtin_Map_Element",
                               Types.variable, Sides.right),
                        Option("builtin_Map_Index",
                               Types.number, Sides.right),
                    ], is_instance=True)


def min_function():
    return Function("Min Function",
                    Min,
                    [
                        Option("builtin_Min",
                               Types.executable, Sides.left),
                        Option("builtin_Min_Data1",
                               Types.variable, Sides.left),
                        Option("builtin_Min_Data2",
                               Types.variable, Sides.left),
                    ],
                    [
                        Option("builtin_Min",
                               Types.executable, Sides.right),
                        Option("builtin_Min_Output",
                               Types.variable, Sides.right),
                        Option("builtin_Min_Index",
                               Types.number, Sides.right),
                    ], is_instance=True)


def max_function():
    return Function("Max Function",
                    Max,
                    [
                        Option("builtin_Max",
                               Types.executable, Sides.left),
                        Option("builtin_Max_Data1",
                               Types.variable, Sides.left),
                        Option("builtin_Max_Data2",
                               Types.variable, Sides.left),
                    ],
                    [
                        Option("builtin_Max",
                               Types.executable, Sides.right),
                        Option("builtin_Max_Output",
                               Types.variable, Sides.right),
                        Option("builtin_Max_Index",
                               Types.number, Sides.right),
                    ], is_instance=True)


def zip_function():
    return Function("Zip Function",
                    Zip,
                    [
                        Option("builtin_Zip",
                               Types.executable, Sides.left),
                        Option("builtin_Zip_Data1",
                               Types.array, Sides.left),
                        Option("builtin_Zip_Data2",
                               Types.array, Sides.left),
                    ],
                    [
                        Option("builtin_Zip",
                               Types.executable, Sides.right),
                        Option("builtin_Zip_Functionality",
                               Types.executable, Sides.right),
                        Option("builtin_Zip_Element",
                               Types.array, Sides.right),
                        Option("builtin_Zip_Index",
                               Types.number, Sides.right),
                    ], is_instance=True)


def exit_function():
    return Function("Exit Function",
                    Exit,
                    [
                        Option("builtin_Exit",
                               Types.executable, Sides.left),
                    ],
                    [], is_instance=True)


#                                    Box Functions                                         #
############################################################################################
