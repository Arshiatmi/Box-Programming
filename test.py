from Utils.extention_manager import *
from Utils.builtins import define_variable, make_box
from Utils.variables import *
from Utils.blocks import *
from Utils.helpers import *

# -------------------------------------------------------------------------------------

##################################################################
#                          Boolean Variable                      #
get_can_use, set_can_use = define_variable("Can Use ?", Types.boolean)

set_can_use(True)
print(get_can_use())

#                          Boolean Variable                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                          Number Variable                       #
get_age, set_age = define_variable("Age", Types.number)

set_age(10)
print(get_age())

#                          Number Variable                       #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                          String Variable                       #

get_name, set_name = define_variable("Name", Types.text)

set_name("Arshia")
print(get_name())

#                          String Variable                       #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                           Array Variable                       #

get_data, set_data = define_variable("data", Types.array)

set_data([1,2,3,4])
print(get_data())

#                           Array Variable                       #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Add Numbers Operator Test                    #

add = make_box(OperatorBuiltins.Add_Two_Numbers, BoxTypes.Operator)
add.attach(get_age, 0, 0, Sides.left)
add.attach(None, 1, 20, Sides.left)
print(add.outputs[0].value)

#                   Add Numbers Operator Test                    #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                 Minus Numbers Operator Test                    #

minus = make_box(OperatorBuiltins.Minus_Two_Numbers, BoxTypes.Operator)
minus.attach(get_age, 0, 0, Sides.left)
minus.attach(None, 1, 5, Sides.left)
print(minus.outputs[0].value)

#                 Minus Numbers Operator Test                    #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                  Add Strings Operator Test                     #

addText = make_box(OperatorBuiltins.Add_Two_Text, BoxTypes.Operator)
addText.attach(get_name, 0, 0, Sides.left)
addText.attach(None, 1, " Is Here", Sides.left)
print(addText.outputs[0].value)

#                  Add Strings Operator Test                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                    AND bool Operator Test                      #

andBool = make_box(OperatorBuiltins.AND, BoxTypes.Operator)
andBool.attach(get_can_use, 0, 0, Sides.left)
andBool.attach(None, 1, False, Sides.left)
print(andBool.outputs[0].value)

#                    AND bool Operator Test                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                     OR bool Operator Test                      #

orBool = make_box(OperatorBuiltins.OR, BoxTypes.Operator)
orBool.attach(get_can_use, 0, 0, Sides.left)
orBool.attach(None, 1, False, Sides.left)
print(orBool.outputs[0].value)

#                     OR bool Operator Test                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                Test Operator With 2 Variable                   #

get_running, set_running = define_variable("Running?", Types.boolean)
set_running(True)

andBool1 = make_box(OperatorBuiltins.AND, BoxTypes.Operator)
andBool1.attach(get_running, 0, 0, Sides.left)
andBool1.attach(get_can_use, 1, 0, Sides.left)
print(andBool1.outputs[0].value)

#                Test Operator With 2 Variable                   #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test If Statements                       #
_if = make_box(ExecutableBuiltins.If, BoxTypes.Executable)
_if.attach(get_running, 1, 0, Sides.left)
_if.attach(set_running, 0, 0, Sides.right)
print(_if.execute_box())  # Returns Next Box

#                       Test If Statements                       #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test Array Type                         #
array_test = Function("arrayTest", array_test, [
    Option("arrayTest", Types.array, Sides.left)])
bx = Box("arrayTest", BoxTypes.Executable, array_test)
bx()

#                        Test Array Type                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test Get Input                           #
#                   Get Name And Say Hello !                     #

_input = make_box(ExecutableBuiltins.Input, BoxTypes.Executable)
_input.attach(None, 1, "Enter Your Name: ", Sides.left)
# Set Answer Will Not Set New Answers Just Runs Function ( Needs For get inputs )
_input.execute_box()
# _input.outputs[1].value Is The Answer As String

say_hello = make_box(OperatorBuiltins.Add_Two_Text, BoxTypes.Operator)
say_hello.attach(None, 0, "Hello ", Sides.left)
say_hello.attach(None, 1, _input.outputs[1].value, Sides.left)
print(say_hello.outputs[0].value)

#                   Get Name And Say Hello !                     #
#                       Test Get Input                           #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                     Test Print Function                        #

_print = make_box(ExecutableBuiltins.Print, BoxTypes.Executable)
_print.attach(None, 1, "Hello There :)", Sides.left)  # Check For Normal Print
_print.execute_box()
_print.attach(get_name, 1, 0, Sides.left)  # Check For Variable
_print.execute_box()
_print.attach(_input, 1, 1, Sides.left)  # Check For Box Chain
_print.execute_box()

#                     Test Print Function                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Text To Number                     #

set_name("1")
textToNumber = make_box(CastBuiltins.Text_To_Number, BoxTypes.Executable)
textToNumber.attach(get_name,1,0)
next_box = textToNumber.execute_box()
print(textToNumber.outputs[2].value) # Prints Casted Variable

#                   Test Cast Text To Number                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                    Test Cast Text To Bool                      #

set_name("")
textToBool = make_box(CastBuiltins.Text_To_Bool, BoxTypes.Executable)
textToBool.attach(get_name,1,0)
next_box = textToBool.execute_box()
print(textToBool.outputs[2].value) # Prints Casted Variable

#                    Test Cast Text To Bool                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Text To Array                      #

set_name("Test")
textToArray = make_box(CastBuiltins.Text_To_Array, BoxTypes.Executable)
textToArray.attach(get_name,1,0)
next_box = textToArray.execute_box()
print(textToArray.outputs[2].value) # Prints Casted Variable

#                   Test Cast Text To Array                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Bool To Number                     #

set_can_use(False)
boolToNumber = make_box(CastBuiltins.Bool_To_Number, BoxTypes.Executable)
boolToNumber.attach(get_can_use,1,0)
next_box = boolToNumber.execute_box()
print(boolToNumber.outputs[2].value) # Prints Casted Variable

#                   Test Cast Bool To Number                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                    Test Cast Bool To Text                      #

set_can_use(True)
boolToText = make_box(CastBuiltins.Bool_To_Text, BoxTypes.Executable)
boolToText.attach(get_can_use,1,0)
next_box = boolToText.execute_box()
print(boolToText.outputs[2].value) # Prints Casted Variable

#                    Test Cast Bool To Text                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Number To Bool                     #

set_age(20)
numberToBool = make_box(CastBuiltins.Number_To_Bool, BoxTypes.Executable)
numberToBool.attach(get_age,1,0)
next_box = numberToBool.execute_box()
print(numberToBool.outputs[2].value) # Prints Casted Variable

#                   Test Cast Number To Bool                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Number To Text                     #

set_age(20)
numberToText = make_box(CastBuiltins.Number_To_Text, BoxTypes.Executable)
numberToText.attach(get_age,1,0)
next_box = numberToText.execute_box()
print(numberToText.outputs[2].value) # Prints Casted Variable

#                   Test Cast Number To Text                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                    Test Cast Array To Text                     #

set_data([6,5,4])
arrayToText = make_box(CastBuiltins.Array_To_Text, BoxTypes.Executable)
arrayToText.attach(get_data,1,0)
next_box = arrayToText.execute_box()
print(arrayToText.outputs[2].value) # Prints Casted Variable

#                    Test Cast Array To Text                     #
##################################################################

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

##################################################################
#                 Test Cast Variable To Text                     #

set_data([6,5,4])
variableToText = make_box(CastBuiltins.Variable_To_Text, BoxTypes.Executable)
variableToText.attach(get_data,1,0)
next_box = variableToText.execute_box()
print(variableToText.outputs[2].value) # Prints Casted Variable

#                 Test Cast Variable To Text                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test Parse Array                         #

parseArray = make_box(ArrayBuiltins.Parse, BoxTypes.Executable)
parseArray.attach(get_data,0,0)
next_box = parseArray.execute_box()
print(parseArray.outputs[0]) # Prints Length Of Array
print(parseArray.outputs[1]) # Prints Array
print(parseArray.outputs[2]) # Prints Reversed Array

#                       Test Parse Array                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test For Loops                          #

forLoop = make_box(ExecutableBuiltins.For, BoxTypes.Executable)
forLoop.attach(get_data,4,0)
variableToText.attach(forLoop,0,1)
variableToText.attach(forLoop,1,3)
_print.attach(variableToText,1,2)
_print.attach(variableToText,0,0)

# Make Finished

next_box = forLoop.execute_box()
print(next_box)

#                        Test For Loops                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test Write File                          #

writeFile = make_box(FileBuiltins.WriteFile, BoxTypes.Executable)
writeFile.attach(None,1,"test/test.txt")
writeFile.attach(None,2,"This Is Test Text To Write In A File\nYay :)")
# Make Finished
next_box = writeFile.execute_box()
print(writeFile.outputs[1].value)

#                       Test Write File                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test Read File                          #

readFile = make_box(FileBuiltins.ReadFile, BoxTypes.Executable)
readFile.attach(None,1,"test/test.txt")
# Make Finished
next_box = readFile.execute_box()
print(next_box)
print(readFile.outputs[1].value)

#                        Test Read File                          #
##################################################################