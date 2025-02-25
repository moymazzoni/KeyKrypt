"""MODULE main.py handles general operations, start and ending."""
from file_operations import locate_directory, refresh_files, display_files
import error_handler, terminal, gui
from utilities import *

def main():
    while True:
        userInput = input(f'{w}{b}>> Type "Window"{e}{w} or {b}"Terminal"{e}{w} for the respective mode...\n  {u}>{e} ')
        directory = locate_directory()  # Looks for 'default' dir location.
        if userInput.lower() in ['window', 'win']:
            print(f'{w}{b}>> Entering... {i}Window Mode{e}{w}.{e}')
            gui.gui()
            return
        elif userInput.lower() in ['terminal', 'term']:
            print(f'{y}{b}>> Entering... {i}Terminal Mode{e}{y}.{e}')
            refresh_files(directory)
            display_files(directory) # Lists file options before entering terminal.
            terminal.terminal(directory)
            return
        else:
            error_handler.error_catcher(0)

if __name__ == '__main__':
    main()