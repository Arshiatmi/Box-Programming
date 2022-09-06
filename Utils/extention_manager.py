from Utils.global_vars import logger
import os

try:
    extentions = ['.'.join(i.split('.')[:-1])
                  for i in os.listdir('extentions') if i.endswith(".py")]
except:
    os.mkdir("extentions")
    extentions = []


def execute_extention(name):
    if name in extentions:
        f = open(os.path.join('extentions', name + ".py"))
        dt = f.read()
        exec(dt, globals())
        f.close()
    else:
        logger.error(f"Could not find extention with name {name}.")


# It Will Be Made After Creation Of Website
def verify_extention(self, name):
    pass
