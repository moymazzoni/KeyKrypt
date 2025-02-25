"""MODULE terminal.py handles the terminal portion, including layered command lines (L1 and L2, file, commands)."""
from terminal_commands import GlobalCommands
from utilities import *

def terminal(directory):
    """FUNCTION terminal() handles the first layer of commands (before entering file)."""
    commands = GlobalCommands()
    key = 'terminal'
    currentFile = None
    while True:
        userInput = input(f'{w}{b}>> [L1]{e}{w} - Enter a command:\n  {u}>{e} ')
        cmd = commands.process_command(userInput, directory, key, currentFile)
        if cmd == 'exit':
            print(f'{y}{b}>> Exiting program...{e}')
            break
        if cmd == 'read':
            print(f'{y}{b}>> Entered {i}file commands.{e}')
            userInput_parts = list(filter(None, userInput.split(' ')))
            if len(userInput_parts) > 1:
                currentFile = userInput_parts[1]
            else:
                currentFile = None
            terminal_2(currentFile, directory, commands)

def terminal_2(currentFile, directory, commands):
    """FUNCTION terminal was so good that we just had to make a sequel."""
    key2 = 'terminal_2'
    while True:
        userInput2 = input(f'{w}{b}>> [L2]{e}{w} - Enter a command:'
                           f'\n     ↪ (in: "{currentFile}")\n  {u}>{e} ')
        cmd2 = commands.process_command(userInput2, directory, key2, currentFile)
        if cmd2 == 'exit':
            print(f'{y}{b}>> Exited {i}file commands.{e}')
            return