"""MODULE terminal.py handles the terminal portion, including layered command lines."""
from terminal_commands import GlobalCommands
from utilities import *

def terminal(directory):
    commands = GlobalCommands()
    key = 'terminal'
    currentFile = None
    while True:
        userInput = input(f'{w}{b}>> [L1]{e}{w} - Enter a command:\n  {u}>{e} ')
        cmd = commands.process_command(userInput, directory, key, currentFile) # Sending full userInput into process_command().
        if cmd == 'exit':
            print(f'{y}{b}>> Exiting program...{e}')
            break
        if cmd == 'read':
            print(f'{y}{b}>> Entering... {i}file commands.{e}')
            currentFile = userInput[3:len(userInput)]
            terminal_2(currentFile, directory, commands)

"""FUNCTION terminal was so good that we just had to make a sequel."""
def terminal_2(currentFile, directory, commands):
    key2 = 'terminal_2'
    while True:
        userInput2 = input(f'{w}{b}>> [L2]{e}{w} - Enter a command:\n  {u}>{e} ')
        cmd2 = commands.process_command(userInput2, directory, key2, currentFile)
        if cmd2 == 'exit':
            print(f'{y}{b}>> Exiting program...{e}')
            return