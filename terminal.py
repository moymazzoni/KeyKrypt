"""MODULE terminal.py handles the terminal portion, including layered command lines."""
from terminal_commands import GlobalCommands
from utilities import *

def terminal(directory):
    commands = GlobalCommands()
    while True:
        userInput = input(f'{w}{b}>> [L1]{e}{w} - Enter a command:\n  {u}>{e} ')
        cmd = commands.process_command(userInput, directory) # Sending full userInput into process_command().
        if cmd is True:
            print(f'{y}{b}>> Exiting program...{e}')
            break
        terminal_2(userInput, directory, commands)

"""FUNCTION terminal was so good that we just had to make a sequel."""
def terminal_2(userInput, directory, commands):
    userInput = input(f'{w}{b}>> [L2]{e}{w} - Enter a command:\n  {u}>{e} ')
    print(userInput)