var boxes = [];

Types = {
    "boolean":1,
    "text":2,
    "number":3,
    "array":4,
    "empty":5,
    "variable":7,
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

// Example Of Creating Box
createBox(2,2).then((box_id) => {
    attachBox(box_id,null,0,2);
    return box_id;
}).then((box_id) => {
    attachBox(box_id,null,1,1);
    return box_id;
}).then((box_id) => {
    get_outputs(box_id).then((result) => {
        console.log(result);
    });
});

// If You Want To Use An Extention Box, You Need To Have Box Names And Extention Name.
define_variable("test",1).then((variable) => {
    run_box(variable[0]).then((val) => {
        console.log(val);
    });
});
