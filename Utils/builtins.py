from Utils.helpers import *
from Utils.enums import BoxTypes, Types, Sides
from Utils.blocks import Function, Box, Option


Box(Type=BoxTypes.Start)
Box(Type=BoxTypes.End)
# Box(Type=BoxTypes.Variable,function=Function("Get Number Variable",getNumberVariable,[Types.text],[Types.number]))
# Box(Type=BoxTypes.Variable,function=Function("Get Boolean Variable",getBooleanVariable,[Types.text],[Types.boolean]))
# Box(Type=BoxTypes.Variable,function=Function("Get Text Variable",getTextVariable,[Types.text],[Types.text]))
# Box(Type=BoxTypes.Executable,function=Function("Set Number Variable",setNumberVariable,[Types.text,Types.number],[]))
# Box(Type=BoxTypes.Executable,function=Function("Set Boolean Variable",setBooleanVariable,[Types.text,Types.boolean],[]))
# Box(Type=BoxTypes.Executable,function=Function("Set Text Variable",setTextVariable,[Types.text,Types.text],[]))

variable_funcs = {
    Types.boolean: [getBooleanVariable, setBooleanVariable, "Boolean"],
    Types.number: [getNumberVariable, setNumberVariable, "Number"],
    Types.text: [getTextVariable, setTextVariable, "String"],
}


def define_variable(name, Type):
    get_variable = Function(f"Function Get {name}",
                            variable_funcs[Type][0], [], [Option(f"{name}", Type, Sides.right)])

    set_variable = Function(f"Function Set {name}",
                            variable_funcs[Type][1], [Option(f"Execute_{name}_in", Types.executable, Sides.left), Option(f"{name}", Type, Sides.left)], [Option(f"Execute_{name}_out", Types.executable, Sides.right)])

    box_get_variable = Box(f"Get {variable_funcs[Type][2]} Variable",
                           BoxTypes.Variable, get_variable)
    box_set_variable = Box(f"Set {variable_funcs[Type][2]} Variable",
                           BoxTypes.Variable, set_variable)
    return box_get_variable, box_set_variable
