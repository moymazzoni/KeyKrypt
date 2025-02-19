"""MODULE error_handler.py ensures that any errors get treated efficiently."""
from utilities import *

def error_catcher(x, *args):
    """Function "error_catcher()" catches potential errors that could occur and returns safely."""
    match x:
        case 0: # General input is invalid.
            print(f'{b}{r}>> ERROR: {e}{i}{r}Not a valid command!{e}'
                  f'{r}\n     ↪ Type "-help" for commands!{e}')
            return
        case 1: # General file was not found.
            print(f'{b}{r}>> ERROR: {e}{i}{r}File "{args[0]}" was not found!{e}')
            return
        case 2: # Generic not a full valid command, too little args.
            print(f'{b}{r}>> ERROR: {e}{i}{r}Not a full command, too little arguments.{e}'
                  f'{r}\n     ↪ Type "-help" for commands!{e}')
            return
        case 3: # Generic not a full valid command, too many args.
            print(f'{b}{r}>> ERROR: {e}{i}{r}Not a valid command, too many arguments.{e}'
                  f'{r}\n     ↪ Type "-help" for commands!{e}')
        case 4:
            print(f'{b}{r}>> ERROR: {e}{r}Invalid argument "{i}{args[0]}'
                  f'{e}{r}"! Use "user", "pass", "app", or leave blank.{e}')
        case 5:
            print(f'{b}{r}>> ERROR: {e}{i}{r}'
                  f'Could not find the main title called: "{args[0]}".{e}')