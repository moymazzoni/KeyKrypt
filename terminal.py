from file_operations import read_files
from terminal_commands import GlobalCommands
from utilities import Color

b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END  # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE  # Terminal color format.

def terminal(directory):
    commands = GlobalCommands()
    while True:
        userInput = input(f'{w}{b}>> [L1]{e}{w} - Enter a command:\n  {u}>{e} ')
        cmd = commands.process_command(userInput, directory) # Sending full userInput into process_command().
