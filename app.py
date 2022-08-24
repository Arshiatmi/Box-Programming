from Utils.variables import *
from Utils.blocks import *
from Utils.helpers import *


##################################################################
#                          Boolean Variable                      #
get_can_use = Function("Function Get Can Use ?",
                       getBooleanVariable, [], [Option("Can Use ?", Types.boolean, Sides.right)])

set_can_use = Function("Function Set Can Use ?",
                       setBooleanVariable, [Option("Execute_can_use_in", Types.executable, Sides.left), Option("Can Use ?", Types.boolean, Sides.left)], [Option("Execute_can_use_out", Types.executable, Sides.right)])

box_get_can_use = Box("Get Boolean Variable", BoxTypes.Variable, get_can_use)
box_set_can_use = Box("Set Boolean Variable", BoxTypes.Variable, set_can_use)

box_set_can_use(True)
print(box_get_can_use())

#                          Boolean Variable                      #
##################################################################


##################################################################
#                          Number Variable                       #

get_age = Function("Function Get age",
                       getNumberVariable, [], [Option("age", Types.number, Sides.right)])

set_age = Function("Function Set age",
                       setNumberVariable, [Option("Execute_age_in", Types.executable, Sides.left), Option("age", Types.number, Sides.left)], [Option("Execute_age_out", Types.executable, Sides.right)])

box_get_age = Box("Get Number Variable", BoxTypes.Variable, get_age)
box_set_age = Box("Set Number Variable", BoxTypes.Variable, set_age)

box_set_age(10)
print(box_get_age())

#                          Number Variable                       #
##################################################################

##################################################################
#                          String Variable                       #

get_name = Function("Function Get name",
                       getNumberVariable, [], [Option("name", Types.text, Sides.right)])

set_name = Function("Function Set name",
                       setNumberVariable, [Option("Execute_name_in", Types.executable, Sides.left), Option("name", Types.text, Sides.left)], [Option("Execute_name_out", Types.executable, Sides.right)])

box_get_name = Box("Get String Variable", BoxTypes.Variable, get_name)
box_set_name = Box("Set String Variable", BoxTypes.Variable, set_name)

box_set_name("Arshia")
print(box_get_name())

#                          String Variable                       #
##################################################################