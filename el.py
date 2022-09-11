from Utils.connector import *
import eel

eel.init("web")
eel.start("index.html", size=(1080, 720), block=False)

allFunctions = getAllFunctions()

while True:
    eel.sleep(1.0)
