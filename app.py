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
print(add.outputs[0].value)

minus = make_box(OperatorBuiltins.Minus_Two_Numbers, BoxTypes.Operator)
minus.attach(get_age, 0, 0, Sides.left)
minus.attach(None, 1, 5, Sides.left)
print(minus.outputs[0].value)

addText = make_box(OperatorBuiltins.Add_Two_Text, BoxTypes.Operator)
addText.attach(get_name, 0, 0, Sides.left)
addText.attach(None, 1, " Is Here", Sides.left)
print(addText.outputs[0].value)

andBool = make_box(OperatorBuiltins.AND, BoxTypes.Operator)
andBool.attach(get_can_use, 0, 0, Sides.left)
andBool.attach(None, 1, False, Sides.left)
print(andBool.outputs[0].value)

orBool = make_box(OperatorBuiltins.OR, BoxTypes.Operator)
orBool.attach(get_can_use, 0, 0, Sides.left)
orBool.attach(None, 1, False, Sides.left)
print(orBool.outputs[0].value)


get_running, set_running = define_variable("Running?", Types.boolean)
set_running(True)
set_can_use(True)

andBool1 = make_box(OperatorBuiltins.AND, BoxTypes.Operator)
andBool1.attach(get_running, 0, 0, Sides.left)
andBool1.attach(get_can_use, 1, 0, Sides.left)
print(andBool1.outputs[0].value)
