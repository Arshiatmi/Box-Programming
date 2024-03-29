import os
import time
from pysha import CrossPlatformer

animation_frames = []

cp = CrossPlatformer()

animation_frames.append(
    """
#############################################################################
|                                                                           |
|                                                                           |
|                                  #                                        |
|                                 ###                                       |
|                               #######                                     |
|                                 ###                                       |
|                               ## | ##                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                                                                           |
|                                                                           |
|           d8888b. d888888b d8888b.   .88b  d88.  .d88b.  .88b  d88.       |
|          88  `8D   `88'   88  `8D   88'YbdP`88 .8P  Y8. 88'YbdP`88        |
|          88oobY'    88    88oodD'   88  88  88 88    88 88  88  88        |
|          88`8b      88    88~~~     88  88  88 88    88 88  88  88        |
|          88 `88.   .88.   88        88  88  88 `8b  d8' 88  88  88        |
|          88   YD Y888888P 88        YP  YP  YP  `Y88P'  YP  YP  YP        |
|                                                                           |
|                                                                           |
#############################################################################
""")

animation_frames.append(
    """
#############################################################################
|                                                                           |
|                                                                           |
|                                   #                                       |
|                                  ###                                      |
|                                ######                                     |
|                                  ##                                       |
|                               ## | ##                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                                                                           |
|                                                                           |
|           d8888b. d888888b d8888b.   .88b  d88.  .d88b.  .88b  d88.       |
|          88  `8D   `88'   88  `8D   88'YbdP`88 .8P  Y8. 88'YbdP`88        |
|          88oobY'    88    88oodD'   88  88  88 88    88 88  88  88        |
|          88`8b      88    88~~~     88  88  88 88    88 88  88  88        |
|          88 `88.   .88.   88        88  88  88 `8b  d8' 88  88  88        |
|          88   YD Y888888P 88        YP  YP  YP  `Y88P'  YP  YP  YP        |
|                                                                           |
|                                                                           |
#############################################################################
""")

animation_frames.append(
    """
#############################################################################
|                                                                           |
|                                 #                                         |
|                                ###                                        |
|                               #####                                       |
|                               ######                                      |
|                                 ###                                       |
|                               ## | ##                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                                                                           |
|                                                                           |
|           d8888b. d888888b d8888b.   .88b  d88.  .d88b.  .88b  d88.       |
|          88  `8D   `88'   88  `8D   88'YbdP`88 .8P  Y8. 88'YbdP`88        |
|          88oobY'    88    88oodD'   88  88  88 88    88 88  88  88        |
|          88`8b      88    88~~~     88  88  88 88    88 88  88  88        |
|          88 `88.   .88.   88        88  88  88 `8b  d8' 88  88  88        |
|          88   YD Y888888P 88        YP  YP  YP  `Y88P'  YP  YP  YP        |
|                                                                           |
|                                                                           |
#############################################################################
""")

animation_frames.append(
    """
#############################################################################
|                                                                           |
|                                                                           |
|                                ##                                         |
|                               ####                                        |
|                              ######                                       |
|                                 ###                                       |
|                               ## | ##                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                                                                           |
|                                                                           |
|           d8888b. d888888b d8888b.   .88b  d88.  .d88b.  .88b  d88.       |
|          88  `8D   `88'   88  `8D   88'YbdP`88 .8P  Y8. 88'YbdP`88        |
|          88oobY'    88    88oodD'   88  88  88 88    88 88  88  88        |
|          88`8b      88    88~~~     88  88  88 88    88 88  88  88        |
|          88 `88.   .88.   88        88  88  88 `8b  d8' 88  88  88        |
|          88   YD Y888888P 88        YP  YP  YP  `Y88P'  YP  YP  YP        |
|                                                                           |
|                                                                           |
#############################################################################
""")

animation_frames.append(
    """
#############################################################################
|                                                                           |
|                                 #                                         |
|                                 ##                                        |
|                                ####                                       |
|                               ######                                      |
|                                ####                                       |
|                               ## | ##                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                               #######                                     |
|                                                                           |
|                                                                           |
|           d8888b. d888888b d8888b.   .88b  d88.  .d88b.  .88b  d88.       |
|          88  `8D   `88'   88  `8D   88'YbdP`88 .8P  Y8. 88'YbdP`88        |
|          88oobY'    88    88oodD'   88  88  88 88    88 88  88  88        |
|          88`8b      88    88~~~     88  88  88 88    88 88  88  88        |
|          88 `88.   .88.   88        88  88  88 `8b  d8' 88  88  88        |
|          88   YD Y888888P 88        YP  YP  YP  `Y88P'  YP  YP  YP        |
|                                                                           |
|                                                                           |
#############################################################################
""")

cp["clear"] = {"linux": "clear", "windows": "cls", "mac": "clear"}

# Or You Can Do This :
"""
cp.add_os_commands(
    "clear", {"linux": "clear", "windows": "cls", "mac": "clear"})
cp["clear"] = {"linux": "clear", "windows": "cls", "mac": "clear"}
"""

c = 0
while True:
    for i in animation_frames:
        print(i)
        time.sleep(0.05)
        os.system(cp["clear"])
    c += 1
    if c == 4:
        break
