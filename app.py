from Utils.variables import *
from Utils.blocks import *
from Utils.functions import *


def set_value(variable, value):
    variable.value = value


get_can_use = Function("Function Get Can Use ?",
                       getBooleanVariable, [], [Option("Can Use ?", Types.boolean, Sides.right)])

set_can_use = Function("Function Set Can Use ?",
                       setBooleanVariable, [Option("Execute_can_use_in", Types.executable, Sides.left), Option("Can Use ?", Types.boolean, Sides.left)], [Option("Execute_can_use_out", Types.executable, Sides.right)])

b1 = Box("Get Boolean Variable", BoxTypes.Variable, get_can_use)
b2 = Box("Set Boolean Variable", BoxTypes.Variable, set_can_use)

b2(True)
print(b1())
