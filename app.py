from Utils.builtins import define_variable, make_box
from Utils.variables import *
from Utils.blocks import *
from Utils.helpers import *


##################################################################
#                          Boolean Variable                      #
get_can_use, set_can_use = define_variable("Can Use ?", Types.boolean)

set_can_use(True)
print(get_can_use())

#                          Boolean Variable                      #
##################################################################


##################################################################
#                          Number Variable                       #
get_age, set_age = define_variable("Age", Types.number)

set_age(10)
print(get_age())

#                          Number Variable                       #
##################################################################

##################################################################
#                          String Variable                       #

get_name, set_name = define_variable("Name", Types.text)

set_name("Arshia")
print(get_name())

#                          String Variable                       #
##################################################################

add = make_box(OperatorBuiltins.Add_Two_Numbers, BoxTypes.Operator)
add.attach(get_age, 0, 0, Sides.left)
add.attach(None, 1, 20, Sides.left)
print(add.inputs[0].value)
print(add.inputs[1].value)
print(add.outputs[0].value)
