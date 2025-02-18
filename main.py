from file_operations import locate_directory, refresh_files, display_files, read_files
from utilities import Color
import error_handler, terminal, gui
b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE # Terminal color format.

def main():
    while True:
        userInput = input(f'{w}{b}>> Type "Window"{e}{w} or {b}"Terminal"{e}{w} for the respective mode...\n  {u}>{e} ')
        if userInput.lower() in ['window', 'win']:
            print(f'{w}{b}>> Entering... {i}Window Mode{e}{w}.{e}')
            gui.gui()
            return
        elif userInput.lower() in ['terminal', 'term']:
            print(f'{y}{b}>> Entering... {i}Terminal Mode{e}{y}.{e}')
            directory = locate_directory() # Looks for 'default' dir location.
            credentialsArray, directoryLen = refresh_files(directory)
            display_files(directory) # Lists file options.
            terminal.terminal(directory)
        else:
            error_handler.error_catcher(0)

if __name__ == '__main__':
    main()