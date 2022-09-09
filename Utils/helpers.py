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
    first_variable_name = inputs[0].id
    second_variable_name = inputs[1].id
    ans = variables[first_variable_name].value + \
        variables[second_variable_name].value
    outputs[0].value = ans


def minus2Numbers(function_id, inputs, outputs):
    first_variable_name = inputs[0].id
    second_variable_name = inputs[1].id
    ans = variables[first_variable_name].value - \
        variables[second_variable_name].value
    outputs[0].value = ans


def AND(function_id, inputs, outputs):
    first_variable_name = inputs[0].id
    second_variable_name = inputs[1].id
    ans = variables[first_variable_name].value and \
        variables[second_variable_name].value
    outputs[0].value = ans


def OR(function_id, inputs, outputs):
    first_variable_name = inputs[0].id
    second_variable_name = inputs[1].id
    ans = variables[first_variable_name].value or \
        variables[second_variable_name].value
    outputs[0].value = ans


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
        outputs[1].value = False
    return outputs[0]


def delete_file(function_id, inputs, outputs):
    file_name = inputs[1].value
    try:
        os.remove(file_name)
    except:
        outputs[1].value = False
    return outputs[0]


def file_list(function_id, inputs, outputs):
    path = inputs[1].value
    contains_files = inputs[2].value
    contains_directories = inputs[3].value
    try:
        if contains_files and contains_directories:
            outputs[1].value = os.listdir(path)
        elif contains_files:
            outputs[1].value = [i for i in os.scandir(path) if i.is_file()]
        elif contains_directories:
            outputs[1].value = [i for i in os.scandir(path) if i.is_dir()]
    except:
        outputs[2].value = False
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
        outputs[1].value = str(eval(text))
    except:
        outputs[2].value = False
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
        outputs[1].value = len(target_object)
    except:
        outputs[2].value = False
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
                    outputs[2].value = False
                    break
            except:
                outputs[2].value = False
                break
    else:
        outputs[1].value = ans
    return outputs[0]
