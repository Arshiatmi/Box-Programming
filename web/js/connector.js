var boxes = [];

Types = {
    "boolean":1,
    "text":2,
    "number":3,
    "array":4,
    "empty":5,
    "variable":7,
}


box_categories = {
    2:
    {
        "Add_Two_Numbers" : 0,
        "Add_Two_Text" : 1,
        "Minus_Two_Numbers" : 2,
        "AND" : 3,
        "OR" : 4,
        "IN" : 5,
        "POW" : 6
    },
    1:
    {
        0: {
            "If" : 0,
            "Input" : 1,
            "Print" : 2,
            "For" : 3,
        },
        1: {
            "Number_To_Text" : 0,
            "Number_To_Bool" : 1,
            "Bool_To_Number" : 2,
            "Bool_To_Text" : 3,
            "Text_To_Number" : 4,
            "Text_To_Bool" : 5,
            "Array_To_Text" : 6,
            "Text_To_Array" : 7,
            "Variable_To_Text" : 8,
        },
        2: {
            "Parse" : 0,
            "Append" : 1,
            "Prepend" : 2,
            "Count" : 3,
            "Index" : 4,
            "Sort" : 5,
            "Insert" : 6,
            "Remove" : 7,
            "MinArray" : 8,
            "MaxArray" : 9,
        },
        3: {
            "ReadFile" : 0,
            "WriteFile" : 1,
            "RemoveFile" : 2,
            "FileList" : 3,
        },
        4: {
            "Capitalize" : 0,
            "Count" : 1,
            "EndsWith" : 2,
            "Find" : 3,
            "IsAlphabet" : 4,
            "IsAlphabetNumber" : 5,
            "IsUpperCase" : 6,
            "IsLowerCase" : 7,
            "ToUpper" : 8,
            "ToLower" : 9,
        },
        5: {
            "runOsCommand" : 0,
            "Eval" : 1
        },
        6: {
            "ToBinary" : 0,
            "FromBinary" : 1,
            "ToOct" : 2,
            "FromOct" : 3,
            "ToHex" : 4,
            "FromHex" : 5,
        },
        7: {
            "Length" : 0,
            "Sum" : 1,
            "Range" : 2,
            "Ord" : 3,
            "Chr" : 4,
            "Map" : 5,
            "Min" : 6,
            "Max" : 7,
            "Exit" : 8,
            "Zip" : 9,
            "Abs" : 10,
        },
    }
}

async function createBox(box_type,first_index,second_index,from_extention=false) {
    let n = await eel.make_box_connector(box_type, first_index,second_index,from_extention)();
    boxes.push(n);
    return n;
}

async function attachBox(box_id,self_index,target_index,side=0) {
    let n = await eel.attach_connector(box_id, self_index,target_index,side)();
    return n;
}

async function get_outputs(box_id) {
    let n = await eel.outputs_connector(box_id)();
    return n;
}

async function box_details(box_id) {
    let n = await eel.box_details_connector(box_id)();
    return n;
}

async function define_variable(name,type) {
    let n = await eel.define_variable_connector(name,type)();
    return n;
}

async function run_box(name) {
    let n = await eel.run_box(name)();
    return n;
}

async function get_variable(name) {
    let n = await eel.get_variable(name)();
    return n;
}

async function set_variable(name,value) {
    let n = await eel.set_variable(name,value)();
    return n;
}
