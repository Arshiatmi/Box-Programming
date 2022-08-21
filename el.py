from Utils.functions import getExecutableFunctions, getVariableFunctions, getAllFunctions, _from_rgb
import eel

eel.init("web")
eel.start("index.html", size=(1080, 720))

executableFunctions = getExecutableFunctions()
variableFunctions = getVariableFunctions()
allFunctions = getAllFunctions()

print(allFunctions)
