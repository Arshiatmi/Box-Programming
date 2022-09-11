// Example Of Creating Box
createBox(2,2).then((box_id) => {
    console.log(box_id);
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
define_variable("test",Types["boolean"]).then((variable) => {
    run_box(variable[0]).then((val) => {
        console.log(val);
    });
});
