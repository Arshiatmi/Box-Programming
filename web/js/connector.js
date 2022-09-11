var boxes = [];

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
