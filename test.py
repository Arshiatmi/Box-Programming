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

set_data([1, 2, 3, 4])
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
textToNumber.attach(get_name, 1, 0)
next_box = textToNumber.execute_box()
print(textToNumber.outputs[2].value)  # Prints Casted Variable

#                   Test Cast Text To Number                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                    Test Cast Text To Bool                      #

set_name("")
textToBool = make_box(CastBuiltins.Text_To_Bool, BoxTypes.Executable)
textToBool.attach(get_name, 1, 0)
next_box = textToBool.execute_box()
print(textToBool.outputs[2].value)  # Prints Casted Variable

#                    Test Cast Text To Bool                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Text To Array                      #

set_name("Test")
textToArray = make_box(CastBuiltins.Text_To_Array, BoxTypes.Executable)
textToArray.attach(get_name, 1, 0)
next_box = textToArray.execute_box()
print(textToArray.outputs[2].value)  # Prints Casted Variable

#                   Test Cast Text To Array                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Bool To Number                     #

set_can_use(False)
boolToNumber = make_box(CastBuiltins.Bool_To_Number, BoxTypes.Executable)
boolToNumber.attach(get_can_use, 1, 0)
next_box = boolToNumber.execute_box()
print(boolToNumber.outputs[2].value)  # Prints Casted Variable

#                   Test Cast Bool To Number                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                    Test Cast Bool To Text                      #

set_can_use(True)
boolToText = make_box(CastBuiltins.Bool_To_Text, BoxTypes.Executable)
boolToText.attach(get_can_use, 1, 0)
next_box = boolToText.execute_box()
print(boolToText.outputs[2].value)  # Prints Casted Variable

#                    Test Cast Bool To Text                      #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Number To Bool                     #

set_age(20)
numberToBool = make_box(CastBuiltins.Number_To_Bool, BoxTypes.Executable)
numberToBool.attach(get_age, 1, 0)
next_box = numberToBool.execute_box()
print(numberToBool.outputs[2].value)  # Prints Casted Variable

#                   Test Cast Number To Bool                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Cast Number To Text                     #

set_age(20)
numberToText = make_box(CastBuiltins.Number_To_Text, BoxTypes.Executable)
numberToText.attach(get_age, 1, 0)
next_box = numberToText.execute_box()
print(numberToText.outputs[2].value)  # Prints Casted Variable

#                   Test Cast Number To Text                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                    Test Cast Array To Text                     #

set_data([6, 5, 4])
arrayToText = make_box(CastBuiltins.Array_To_Text, BoxTypes.Executable)
arrayToText.attach(get_data, 1, 0)
next_box = arrayToText.execute_box()
print(arrayToText.outputs[2].value)  # Prints Casted Variable

#                    Test Cast Array To Text                     #
##################################################################

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

##################################################################
#                 Test Cast Variable To Text                     #

set_data([6, 5, 4])
variableToText = make_box(CastBuiltins.Variable_To_Text, BoxTypes.Executable)
variableToText.attach(get_data, 1, 0)
next_box = variableToText.execute_box()
print(variableToText.outputs[2].value)  # Prints Casted Variable

#                 Test Cast Variable To Text                     #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test Parse Array                         #

parseArray = make_box(ArrayBuiltins.Parse, BoxTypes.Executable)
parseArray.attach(get_data, 0, 0)
next_box = parseArray.execute_box()
print(parseArray.outputs[0])  # Prints Length Of Array
print(parseArray.outputs[1])  # Prints Array
print(parseArray.outputs[2])  # Prints Reversed Array

#                       Test Parse Array                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test For Loops                          #

forLoop = make_box(ExecutableBuiltins.For, BoxTypes.Executable)
forLoop.attach(get_data, 4, 0)
variableToText.attach(forLoop, 0, 1)
variableToText.attach(forLoop, 1, 3)
_print.attach(variableToText, 1, 2)
_print.attach(variableToText, 0, 0)

# Make Finished

next_box = forLoop.execute_box()
print(next_box)

#                        Test For Loops                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test Write File                          #

writeFile = make_box(FileBuiltins.WriteFile, BoxTypes.Executable)
writeFile.attach(None, 1, "test/test.txt")
writeFile.attach(None, 2, "This Is Test Text To Write In A File\nYay :)")
next_box = writeFile.execute_box()
print(writeFile.outputs[1].value)

#                       Test Write File                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test Read File                          #

readFile = make_box(FileBuiltins.ReadFile, BoxTypes.Executable)
readFile.attach(None, 1, "test/test.txt")
next_box = readFile.execute_box()
print(readFile.outputs[1].value)

#                        Test Read File                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                      Test Remove File                          #

removeFile = make_box(FileBuiltins.RemoveFile, BoxTypes.Executable)
removeFile.attach(None, 1, "test/test.txt")
next_box = removeFile.execute_box()
print(removeFile.outputs[1].value)

#                      Test Remove File                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                     Test FileList Box                          #

fileList = make_box(FileBuiltins.FileList, BoxTypes.Executable)
next_box = fileList.execute_box()
print(fileList.outputs[1].value)

#                     Test FileList Box                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Append To Array                         #

appendList = make_box(ArrayBuiltins.Append, BoxTypes.Executable)
appendList.attach(get_data, 0, 0)
appendList.attach(None, 1, 43)
print(appendList.outputs[0].value)

#                   Test Append To Array                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                 Test Count Elements In Array                    #

countList = make_box(ArrayBuiltins.Count, BoxTypes.Executable)
countList.attach(get_data, 0, 0)
countList.attach(None, 1, 6)
print(countList.outputs[0].value)
countList.attach(None, 1, 32)
print(countList.outputs[0].value)

#                 Test Count Elements In Array                    #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#              Test Get Index Of Element In Array                #

indexList = make_box(ArrayBuiltins.Index, BoxTypes.Executable)
indexList.attach(get_data, 0, 0)
indexList.attach(None, 1, 6)
print(indexList.outputs[0].value)
indexList.attach(None, 1, 32)
print(indexList.outputs[0].value)

#              Test Get Index Of Element In Array                #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                 Test Insert Element To Array                   #

insertList = make_box(ArrayBuiltins.Insert, BoxTypes.Executable)
insertList.attach(get_data, 0, 0)
insertList.attach(None, 1, 6)
insertList.attach(None, 2, 1)
print(insertList.outputs[0].value)
print(insertList.outputs[1].value)

#                 Test Insert Element To Array                   #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                Test Remove Element From Array                  #


removeList = make_box(ArrayBuiltins.Remove, BoxTypes.Executable)
removeList.attach(get_data, 0, 0)
removeList.attach(None, 1, 6)
print(removeList.outputs[0].value)
print(removeList.outputs[1].value)

#                Test Remove Element From Array                  #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                 Test Prepend Element To Array                  #


prependList = make_box(ArrayBuiltins.Prepend, BoxTypes.Executable)
prependList.attach(get_data, 0, 0)
prependList.attach(None, 1, 6)
print(prependList.outputs[0].value)

#                 Test Prepend Element To Array                  #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test Sort Array                         #


sortList = make_box(ArrayBuiltins.Sort, BoxTypes.Executable)
sortList.attach(prependList, 0, 0)
print(sortList.outputs[0].value)

#                        Test Sort Array                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                     Test Capitalize Text                       #


capitalizeText = make_box(TextBuiltins.Capitalize, BoxTypes.Executable)
capitalizeText.attach(get_name, 0, 0)
print(capitalizeText.outputs[0].value)

#                     Test Capitalize Text                       #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test Count Text                          #


countText = make_box(TextBuiltins.Count, BoxTypes.Executable)
countText.attach(get_name, 0, 0)
countText.attach(None, 1, "e")
print(countText.outputs[0].value)

#                       Test Count Text                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                     Test EndsWith Text                         #


endsWithText = make_box(TextBuiltins.EndsWith, BoxTypes.Executable)
endsWithText.attach(get_name, 0, 0)
endsWithText.attach(None, 1, "t")
print(endsWithText.outputs[0].value)

#                     Test EndsWith Text                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test Find Text                           #


findText = make_box(TextBuiltins.Find, BoxTypes.Executable)
findText.attach(get_name, 0, 0)
findText.attach(None, 1, "t")
print(findText.outputs[0].value)

#                       Test Find Text                           #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                   Test Is Alphabet Text                        #


isalphabetText = make_box(TextBuiltins.IsAlphabet, BoxTypes.Executable)
isalphabetText.attach(get_name, 0, 0)
print(isalphabetText.outputs[0].value)

#                   Test Is Alphabet Text                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#            Test Is Alphabet Or Number Or Both Text             #


isalphabetNumberText = make_box(
    TextBuiltins.IsAlphabetNumber, BoxTypes.Executable)
isalphabetNumberText.attach(get_name, 0, 0)
print(isalphabetNumberText.outputs[0].value)

#            Test Is Alphabet Or Number Or Both Text             #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#            Test Is Digits ( Number ) Or Both Text              #


isdigitsText = make_box(TextBuiltins.IsDigit, BoxTypes.Executable)
isdigitsText.attach(get_name, 0, 0)
print(isdigitsText.outputs[0].value)

#            Test Is Digits ( Number ) Or Both Text              #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                      Test To Lower Text                        #


toLowerText = make_box(TextBuiltins.ToLower, BoxTypes.Executable)
toLowerText.attach(get_name, 0, 0)
print(toLowerText.outputs[0].value)

#                      Test To Lower Text                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                      Test Is Lower Text                        #


isLowerText = make_box(TextBuiltins.IsLowerCase, BoxTypes.Executable)
isLowerText.attach(toLowerText, 0, 0)
print(isLowerText.outputs[0].value)

#                      Test Is Lower Text                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                      Test To Upper Text                        #


toUpperText = make_box(TextBuiltins.ToUpper, BoxTypes.Executable)
toUpperText.attach(get_name, 0, 0)
print(toUpperText.outputs[0].value)

#                      Test To Upper Text                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                      Test Is Upper Text                        #


isUpperText = make_box(TextBuiltins.IsUpperCase, BoxTypes.Executable)
isUpperText.attach(toUpperText, 0, 0)
print(isUpperText.outputs[0].value)

#                      Test Is Upper Text                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                      Test Run Os Command                       #


runOsCommandObj = make_box(Others.runOsCommand, BoxTypes.Executable)
runOsCommandObj.attach(None, 1, "cls")
runOsCommandObj.attach(None, 2, False)
runOsCommandObj.execute_box()

#                      Test Run Os Command                       #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                         Test Join Text                         #


joinText = make_box(TextBuiltins.Join, BoxTypes.Executable)
joinText.attach(None, 0, '.')
joinText.attach(get_data, 1, 0)
print(joinText.outputs[0].value)

#                         Test Join Text                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                       Test Replace Text                        #


replaceText = make_box(TextBuiltins.Replace, BoxTypes.Executable)
replaceText.attach(toLowerText, 0, 0)
replaceText.attach(None, 1, 't')
replaceText.attach(None, 2, 'd')
print(replaceText.outputs[0].value)

#                       Test Replace Text                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test Strip Text                         #


stripText = make_box(TextBuiltins.Strip, BoxTypes.Executable)
stripText.attach(None, 0, "\nWelcome Here ")
print(stripText.outputs[0].value)

#                        Test Strip Text                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test Split Text                         #


splitText = make_box(TextBuiltins.Split, BoxTypes.Executable)
splitText.attach(None, 0, "Welcome Here ")
splitText.attach(None, 1, " ")
print(splitText.outputs[0].value)

#                        Test Split Text                         #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                      Test Swapcase Text                        #


swapcaseText = make_box(TextBuiltins.SwapCase, BoxTypes.Executable)
swapcaseText.attach(None, 0, "Welcome Here ")
print(swapcaseText.outputs[0].value)

#                      Test Swapcase Text                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                      Test Zerofill Text                        #


zerofillText = make_box(TextBuiltins.ZeroFill, BoxTypes.Executable)
zerofillText.attach(None, 0, "10")
zerofillText.attach(None, 1, 5)
print(zerofillText.outputs[0].value)

#                      Test Zerofill Text                        #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                        Test Eval Text                          #


evalText = make_box(Others.Eval, BoxTypes.Executable)
evalText.attach(None, 1, "1 + 1")
evalText.execute_box()
print(evalText.outputs[1].value)

#                        Test Eval Text                          #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                     Test Get Length Text                       #


getLength = make_box(Boxfunctions.Length, BoxTypes.Executable)
getLength.attach(get_data, 1, 0)
getLength.execute_box()
print(getLength.outputs[1].value)

#                     Test Get Length Text                       #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                           Test Sum                             #

sumData = make_box(Boxfunctions.Sum, BoxTypes.Executable)
sumData.attach(get_data, 1, 0)
sumData.addOption(Option("builtin_Number2", Types.number, Sides.left))
sumData.attach(None, 2, 10)
sumData.execute_box()
print(sumData.outputs[1].value)

#                           Test Sum                             #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                         Test Range                             #

getRange = make_box(Boxfunctions.Range, BoxTypes.Executable)
getRange.attach(None, 1, 10)
getRange.attach(None, 2, 5)
getRange.attach(None, 3, -1)
getRange.execute_box()
print(getRange.outputs[1].value)

#                         Test Range                             #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                          Test Ord                              #

getOrd = make_box(Boxfunctions.Ord, BoxTypes.Executable)
getOrd.attach(None, 1, "Yo :)")
getOrd.execute_box()
print(getOrd.outputs[1].value)

#                          Test Ord                              #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                          Test Chr                              #

getChr = make_box(Boxfunctions.Chr, BoxTypes.Executable)
getChr.attach(getOrd, 1, 1)
getChr.attach(None, 2, True)
getChr.execute_box()
print(getChr.outputs[1].value)

#                          Test Chr                              #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                          Test Map                              #

testMap = make_box(Boxfunctions.Map, BoxTypes.Executable)
variableToText.attach(testMap, 0, 1)
variableToText.attach(testMap, 1, 2)
_print.attach(variableToText, 0, 0)
_print.attach(variableToText, 1, 2)
testMap.attach(None, 1, [1, 2, 3])
print(testMap.execute_box())

#                          Test Map                              #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                          Test Min                              #

testMin = make_box(Boxfunctions.Min, BoxTypes.Executable)
testMin.attach(None, 1, 100)
testMin.attach(None, 2, 268)
testMin.execute_box()
print(testMin.outputs[1].value)  # Minimum Element
print(testMin.outputs[2].value)  # Minimum Index

#                          Test Min                              #
##################################################################

# -------------------------------------------------------------------------------------

##################################################################
#                          Test Max                              #

testMax = make_box(Boxfunctions.Max, BoxTypes.Executable)
testMax.attach(None, 1, 100)
testMax.attach(None, 2, 268)
testMax.execute_box()
print(testMax.outputs[1].value)  # Maximum Element
print(testMax.outputs[2].value)  # Maximum Index

#                          Test Max                              #
##################################################################
