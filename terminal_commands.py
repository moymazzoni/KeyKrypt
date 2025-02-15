import error_handler
from file_operations import display_files, read_files
from utilities import Color
b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE # Terminal color format.

class GlobalCommands: # Hosts all commands.
    def __init__(self):
        self.commands = {
            '-help': self.help_file_command,
            '-h': self.help_command,
            '-list': self.list_command,
            '-l': self.list_command,
            '-exit': self.exit_command,
            '-e': self.exit_command,
            '-copy': self.copy_command,
            '-c': self.copy_command,
            '-read': self.read_command,
            '-r': self.read_command
        }
    def process_command(self, userInput, directory):
        userInput = userInput.split()
        print(userInput)
        try:
            action = self.commands.get(userInput[0], lambda: error_handler.error_catcher(2))
            action(userInput, directory)
        except (TypeError, IndexError): # Catches empty inputs or invalid ones (not a command).
            error_handler.error_catcher(0)

    @staticmethod
    def list_command(_, directory):
        display_files(directory)
        return

    @staticmethod
    def help_command(*args):
        print(f'{Color.BOLD}{Color.UNDERLINE}Selection Help page:{Color.END}'
              f'\n╭ [1] -help -> brings up a list of commands.'
              f'\n| [2] -list -> lists all files in directory.'
              f'\n| [3] -exit -> exit the program entirely.'
              f'\n╰ [4] -read -> re-read the current file.')
        return

    @staticmethod
    def help_file_command(*args):
         print(f'{Color.BOLD}{Color.UNDERLINE}File Help page:{Color.END}'
              f'\n╭ [1] -help -> brings up a list of commands.'
              f'\n| [2] -list -> lists all files in directory.'
              f'\n| [3] -exit -> exit the current subsection.'
              f'\n| [4] -copy -> alone, copies email & password. Chained with "user", "pass", or "app" for respective copies.'
              f'\n|  ↪   ex: -copy app_name, -copy app_name user, -copy app_name pass, -copy app_name app'
              f'\n╰ [5] -read -> re-read the current file.')

    @staticmethod
    def exit_command():
        print('Hi from exit_command!')
        return

    @staticmethod
    def read_command(userInput, directory):
        if len(userInput) > 2:
            return error_handler.error_catcher(3)
        try:
            read_files(userInput[1], directory)
        except IndexError:
            error_handler.error_catcher(2)
            return
        except FileNotFoundError:
            error_handler.error_catcher(1, userInput[1])  # If file is not found.
            return

    @staticmethod
    def copy_command(userInput, directory):
        print()