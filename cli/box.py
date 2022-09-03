from pysha import *
import sys

try:
    command = sys.argv[1]
except:
    print("""You Need To Insert Command.
Usage : 
    box.py command [arguments]

Commands : 
    install    ->   To Install Extention. It Needs One Argument Containing Extention Name.
    uninstall  ->   To Remove Extention. It Needs One Argument Containing Extention Name.
    verify     ->   It Will Verify All Of Your Extentions And Warns You On Unverified Extentions.
    list       ->   Gets Extention List For You.
    help       ->   Show This Help Message.
""")
    exit(1)


def install_command(name):
    pass


def uninstall_command(name):
    pass


def verify_command():
    pass


def list_command():
    pass


def help_command():
    print("""You Need To Insert Command.
Usage : 
    box.py command [arguments]

Commands : 
    install    ->   To Install Extention. It Needs One Argument Containing Extention Name.
    uninstall  ->   To Remove Extention. It Needs One Argument Containing Extention Name.
    verify     ->   It Will Verify All Of Your Extentions And Warns You On Unverified Extentions.
    list       ->   Gets Extention List For You.
    help       ->   Show This Help Message.
""")


try:
    Switch(command).cases({
        Case("install"):
            [install_command, [sys.argv[2]]],
        Case("uninstall"):
            [uninstall_command, [sys.argv[2]]],
        Case("verify"):
            [verify_command],
        Case("list"):
            [list_command],
        Case("help"):
            [help_command],
    })
except:
    print("You Need To Insert Argument For Your Command Too ( Extention Name ).")
    exit(1)
