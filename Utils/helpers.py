import sys
import os
from .global_vars import *
from .variables import Variable, variables
from .enums import BoxTypes, Types


def getExecutableFunctions():
    return {i: j for i, j in boxes.items() if j.type == BoxTypes.Executable}


def getVariableFunctions():
    return {i: j for i, j in boxes.items() if j.type == BoxTypes.Variable}


def getOperatorFunctions():
    return {i: j for i, j in boxes.items() if j.type == BoxTypes.Operator}


def getEventFunctions():
    return {i: j for i, j in boxes.items() if j.type == BoxTypes.Event}


def getAllFunctions():
    return boxes


def getBooleanVariable(function_id, inputs, outputs):
    variable_name = outputs[0].variable.id
    return variables[variable_name]


def getNumberVariable(function_id, inputs, outputs):
    variable_name = outputs[0].variable.id
    return variables[variable_name]


def getTextVariable(function_id, inputs, outputs):
    variable_name = outputs[0].variable.id
    return variables[variable_name]


def getArrayVariable(function_id, inputs, outputs):
    variable_name = outputs[0].variable.id
    return variables[variable_name]


def setBooleanVariable(function_id, inputs, outputs, value):
    inputs[1].variable.value = value
    return value


def setNumberVariable(function_id, inputs, outputs, value):
    inputs[1].variable.value = value
    return value


def setTextVariable(function_id, inputs, outputs, value):
    inputs[1].variable.value = value
    return value


def setArrayVariable(function_id, inputs, outputs, value):
    inputs[1].variable.value = value
    return inputs[1].variable


def add2vars(function_id, inputs, outputs):
    ans = inputs[0].value + inputs[1].value
    outputs[0].value = ans


def minus2Numbers(function_id, inputs, outputs):
    ans = inputs[0].value - inputs[1].value
    outputs[0].value = ans


def AND(function_id, inputs, outputs):
    ans = inputs[0].value and inputs[1].value
    outputs[0].value = ans


def OR(function_id, inputs, outputs):
    ans = inputs[0].value or inputs[1].value
    outputs[0].value = ans


def POW(function_id, inputs, outputs):
    ans = inputs[0].value ** inputs[1].value
    outputs[0].value = ans


def IN(function_id, inputs, outputs):
    try:
        ans = inputs[0].value in inputs[1].value
        outputs[0].value = ans
    except:
        outputs[1].value = False


def if_statement(function_id, inputs, outputs):
    if inputs[1].value:
        return outputs[0]
    else:
        return outputs[1]


def get_input(function_id, inputs, outputs):
    outputs[1].value = input(inputs[1].value)
    return outputs[0]


def print_string(function_id, inputs, outputs):
    print(inputs[1].value)
    return outputs[0]


def number_to_text(function_id, inputs, outputs):
    try:
        outputs[2].value = str(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def number_to_bool(function_id, inputs, outputs):
    try:
        outputs[2].value = bool(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def bool_to_number(function_id, inputs, outputs):
    try:
        outputs[2].value = float(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def bool_to_text(function_id, inputs, outputs):
    try:
        outputs[2].value = str(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def text_to_number(function_id, inputs, outputs):
    try:
        outputs[2].value = float(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def text_to_bool(function_id, inputs, outputs):
    try:
        outputs[2].value = bool(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def array_to_text(function_id, inputs, outputs):
    try:
        outputs[2].value = str(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def text_to_array(function_id, inputs, outputs):
    try:
        outputs[2].value = list(inputs[1].value)
        return outputs[0]
    except:
        return outputs[1]


def variable_to_text(function_id, inputs, outputs):
    try:
        target_object = inputs[1].value
        if Variable.is_number(target_object):
            if int(target_object) == target_object:
                target_object = int(target_object)
        outputs[2].value = str(target_object)
        return outputs[0]
    except:
        return outputs[1]


def parse_array(function_id, inputs, outputs):
    outputs[0].value = len(inputs[0].value)
    outputs[1].value = list(inputs[0].value)
    outputs[2].value = list(reversed(inputs[0].value))


def append_array(function_id, inputs, outputs):
    array = inputs[0].value.copy()
    array.append(inputs[1].value)
    outputs[0].value = array


def prepend_array(function_id, inputs, outputs):
    array = inputs[0].value.copy()
    array.insert(0, inputs[1].value)
    outputs[0].value = array


def count_elements_array(function_id, inputs, outputs):
    array = inputs[0].value
    count = array.count(inputs[1].value)
    outputs[0].value = count


def index_element_array(function_id, inputs, outputs):
    array = inputs[0].value
    try:
        index = array.index(inputs[1].value)
    except:
        index = -1
    outputs[0].value = index


def insert_element_array(function_id, inputs, outputs):
    array = inputs[0].value.copy()
    try:
        array.insert(inputs[2].value, inputs[1].value)
        outputs[0].value = array
    except:
        outputs[1].value = False


def sort_array(function_id, inputs, outputs):
    array = inputs[0].value.copy()
    array.sort()
    outputs[0].value = array


def remove_element_array(function_id, inputs, outputs):
    array = inputs[0].value.copy()
    element = inputs[1].value
    is_index = inputs[2].value
    try:
        if is_index:
            array.pop(element)
        else:
            array.remove(element)
        outputs[0].value = array
    except ValueError:
        pass
    except:
        outputs[1].value = False


def minimum_element_in_array(function_id, inputs, outputs):
    array = inputs[0].value.copy()
    minimum_element = min(array)
    minimum_index = array.index(minimum_element)
    outputs[0].value = minimum_element
    outputs[1].value = minimum_index


def maximum_element_in_array(function_id, inputs, outputs):
    array = inputs[0].value.copy()
    maximum_element = max(array)
    maximum_index = array.index(maximum_element)
    outputs[0].value = maximum_element
    outputs[1].value = maximum_index


def read_file(function_id, inputs, outputs):
    file_name = inputs[1].value
    f = open(file_name, "r")
    data = f.readlines()
    f.close()
    outputs[2].value = data
    outputs[1].value = ''.join(data)
    return outputs[0]


def write_file(function_id, inputs, outputs):
    file_name = inputs[1].value
    text = inputs[2].value
    try:
        if inputs[3].value == True:
            f = open(file_name, "a")
        else:
            f = open(file_name, "w")
        f.write(text)
        f.close()
    except:
        return outputs[1]
    return outputs[0]


def delete_file(function_id, inputs, outputs):
    file_name = inputs[1].value
    try:
        os.remove(file_name)
    except:
        return outputs[1]
    return outputs[0]


def file_list(function_id, inputs, outputs):
    path = inputs[1].value
    contains_files = inputs[2].value
    contains_directories = inputs[3].value
    try:
        if contains_files and contains_directories:
            outputs[2].value = os.listdir(path)
        elif contains_files:
            outputs[2].value = [i for i in os.scandir(path) if i.is_file()]
        elif contains_directories:
            outputs[2].value = [i for i in os.scandir(path) if i.is_dir()]
    except:
        return outputs[1]
    return outputs[0]


def capitalize_text(function_id, inputs, outputs):
    text = inputs[0].value
    outputs[0].value = text.capitalize()


def count_text(function_id, inputs, outputs):
    text = inputs[0].value
    search_text = inputs[1].value
    outputs[0].value = text.count(search_text)


def endswith_text(function_id, inputs, outputs):
    text = inputs[0].value
    search_text = inputs[1].value
    outputs[0].value = text.endswith(search_text)


def find_text(function_id, inputs, outputs):
    text = inputs[0].value
    search_text = inputs[1].value
    reverse_search = inputs[2].get(False)
    if reverse_search:
        outputs[0].value = text.rfind(search_text)
    else:
        outputs[0].value = text.find(search_text)


def join_text(function_id, inputs, outputs):
    text = inputs[0].value
    array = inputs[1].value
    array = list(map(lambda x: str(x), array))
    outputs[0].value = text.join(array)


def replace_text(function_id, inputs, outputs):
    text = inputs[0].value
    search_text = inputs[1].value
    replace_text = inputs[2].value
    outputs[0].value = text.replace(search_text, replace_text)


def strip_text(function_id, inputs, outputs):
    text = inputs[0].get()
    customized_strip = inputs[1].get(None)
    strip_left = inputs[2].get(True)
    strip_right = inputs[3].get(True)
    if strip_left and strip_right:
        outputs[0].value = text.strip(customized_strip)
    elif strip_left:
        outputs[0].value = text.lstrip()
    elif strip_right:
        outputs[0].value = text.rstrip()
    else:
        outputs[0].value = text


def split_text(function_id, inputs, outputs):
    text = inputs[0].get()
    splitter = inputs[1].get(" ")
    split_count = inputs[2].get(-1)
    start_index = inputs[3].get(-1)
    end_index = inputs[4].get(-1)
    if start_index != -1:
        text = text[start_index:end_index]
    if split_count != -1:
        outputs[0].value = text.split(splitter, split_count)
    else:
        outputs[0].value = text.split(splitter)


def swapcase_text(function_id, inputs, outputs):
    text = inputs[0].get()
    outputs[0].value = text.swapcase()


def zerofill_text(function_id, inputs, outputs):
    text = inputs[0].get()
    zeroCount = inputs[1].get(1)
    outputs[0].value = text.zfill(zeroCount)


def isalphabet_text(function_id, inputs, outputs):
    text = inputs[0].value
    outputs[0].value = text.isalpha()


def isalphabetnumber_text(function_id, inputs, outputs):
    text = inputs[0].value
    outputs[0].value = text.isalnum()


def isdigit_text(function_id, inputs, outputs):
    text = inputs[0].value
    outputs[0].value = text.isdigit()


def islowercase_text(function_id, inputs, outputs):
    text = inputs[0].value
    outputs[0].value = text.islower()


def isuppercase_text(function_id, inputs, outputs):
    text = inputs[0].value
    outputs[0].value = text.isupper()


def touppercase_text(function_id, inputs, outputs):
    text = inputs[0].value
    outputs[0].value = text.upper()


def tolowercase_text(function_id, inputs, outputs):
    text = inputs[0].value
    outputs[0].value = text.lower()


def runOsCommand(function_id, inputs, outputs):
    text = inputs[1].value
    as_process = inputs[2].value
    if as_process:
        ans = os.popen(text).read()
        outputs[1].value = ans
    else:
        os.system(text)
    return outputs[0]


def pythonEvaluate(function_id, inputs, outputs):
    text = inputs[1].value
    try:
        outputs[2].value = str(eval(text))
    except:
        return outputs[1]
    return outputs[0]


def for_loop(function_id, inputs, outputs):
    start = inputs[1].get(0)
    array = inputs[4].get()
    step = inputs[3].get(1)
    end = inputs[2].get(len(array))
    if array:
        for i in range(start, end, step):
            outputs[2].value = i
            outputs[3].value = array[i]
            next_box = outputs[1].target_option.parent.execute_box()
            while True:
                if not next_box:
                    break
                next_box = next_box.execute_box()
    else:
        for i in range(start, end, step):
            outputs[2].value = i
            next_box = outputs[1].target_option.parent.execute_box()
            while True:
                if not next_box:
                    break
                next_box = next_box.execute_box()
    return outputs[0]


def array_test(function_id, inputs, outputs):
    inputs[0].value.append("test")


def convert_to_list(inputs):
    if not inputs:
        return []
    if type(inputs) == list:
        return inputs
    elif type(inputs) == dict or type(inputs) == tuple or type(inputs) == set or type(inputs) == frozenset:
        ans = []
        for i in inputs:
            ans.append(i.value)
        return ans
    else:
        return [inputs]


def get_length(function_id, inputs, outputs):
    target_object = inputs[1].value
    try:
        outputs[2].value = len(target_object)
    except:
        return outputs[1]
    return outputs[0]


def sum_of_data(function_id, inputs, outputs):
    target_objects = inputs[1:]
    ans = 0
    for i in target_objects:
        try:
            ans += float(i.value)
        except:
            try:
                if i.Type == Types.array or i.Type == Types.variable:
                    ans += sum(i.value)
                else:
                    return outputs[1]
            except:
                return outputs[1]
    else:
        outputs[2].value = ans
    return outputs[0]


def Range(function_id, inputs, outputs):
    start_index = inputs[1].value
    end_index = inputs[2].value
    step = inputs[3].value
    outputs[1].value = list(range(start_index, end_index, step))
    return outputs[0]


def Ord(function_id, inputs, outputs):
    text = inputs[1].value
    ans = []
    try:
        if len(text) == 1:
            outputs[2].value = ord(text)
        else:
            for i in text:
                ans.append(ord(i))
            outputs[2].value = ans
    except:
        return outputs[1]
    return outputs[0]


def Chr(function_id, inputs, outputs):
    inp = inputs[1].value
    as_string = inputs[2].value
    try:
        ans = []
        for i in inp:
            ans.append(chr(i))
        if as_string:
            outputs[2].value = ''.join(ans)
        else:
            outputs[2].value = ans
    except:
        return outputs[1]
    return outputs[0]


def Map(function_id, inputs, outputs):
    inp = inputs[1].value
    for c, i in enumerate(inp):
        outputs[2].value = i
        outputs[3].value = c
        next_box = outputs[1].target_option.parent.execute_box()
        while True:
            if not next_box:
                break
            next_box = next_box.execute_box()
    return outputs[0]


def Min(function_id, inputs, outputs):
    inp = inputs[1:]
    inp = list(map(lambda x: x.value, inp))
    min_value = min(inp)
    outputs[1].value = min_value
    outputs[2].value = inp.index(min_value)
    return outputs[0]


def Max(function_id, inputs, outputs):
    inp = inputs[1:]
    inp = list(map(lambda x: x.value, inp))
    min_value = max(inp)
    outputs[1].value = min_value
    outputs[2].value = inp.index(min_value)
    return outputs[0]


def Zip(function_id, inputs, outputs):
    datas = inputs[1:]
    datas = list(map(lambda x: x.value, datas))
    last_index = len(min(datas, key=len))
    for i in range(last_index):
        outputs[2].value = [elem[i] for elem in datas]
        outputs[3].value = i
        next_box = outputs[1].target_option.parent.execute_box()
        while True:
            if not next_box:
                break
            next_box = next_box.execute_box()
    return outputs[0]


def Abs(function_id, inputs, outputs):
    number = inputs[0].value
    outputs[0].value = abs(number)


def Exit(function_id, inputs, outputs):
    sys.exit(0)


def ToBinary(function_id, inputs, outputs):
    number = inputs[1].value
    outputs[1].value = bin(number)[2:]


def FromBinary(function_id, inputs, outputs):
    number = inputs[1].value
    try:
        outputs[2].value = int(number, 2)
    except:
        return outputs[1]
    return outputs[0]


def ToOct(function_id, inputs, outputs):
    number = inputs[1].value
    try:
        outputs[2].value = oct(number)[2:]
    except:
        return outputs[1]
    return outputs[0]


def FromOct(function_id, inputs, outputs):
    number = inputs[1].value
    try:
        outputs[2].value = int(number, 8)
    except:
        return outputs[1]
    return outputs[0]


def FromHex(function_id, inputs, outputs):
    number = inputs[1].value
    try:
        outputs[2].value = int(number, 16)
    except:
        return outputs[1]
    return outputs[0]


def ToHex(function_id, inputs, outputs):
    number = inputs[1].value
    try:
        outputs[2].value = hex(number)
    except:
        return outputs[1]
    return outputs[0]
