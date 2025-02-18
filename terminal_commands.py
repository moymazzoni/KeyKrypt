"""MODULE terminal_commands.py contains all the commands that ties back to file_operations.py or its own functions."""
import error_handler
from file_operations import display_files, read_files, scan_function
from utilities import *
"""CLASS GlobalCommands contains all commands in a dictionary and the functions for correlating command."""
class GlobalCommands: # Hosts all commands.
    def __init__(self):
        self.commands = {
            '-help': self.help_command,
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

    """FUNCTION process_command() is where the userInput goes in and gets sent to the appropriate function."""
    def process_command(self, userInput, directory):
        userInput = list(filter(None, userInput.split(' ')))  # Chops up the text so only words are passed as args.
        try:
            action = self.commands.get(userInput[0], lambda: error_handler.error_catcher(2))
            isExit = action(userInput, directory) # Track result of correlating command.
            if isExit is True:  # If exit command was input, exit.
                return True
        except (TypeError, IndexError):  # Catches empty inputs or invalid ones
            error_handler.error_catcher(0)
        return False

    @staticmethod
    def list_command(userInput, directory):
        if len(userInput) > 1:
            return error_handler.error_catcher(3)
        return display_files(directory)

    @staticmethod
    def help_command(userInput, _):
        if len(userInput) > 1:
            return error_handler.error_catcher(3)
        print(f'{w}{b}>> {u}Selection Help page:{e}'
              f'\n╭ [1] -help -> brings up a list of commands.'
              f'\n| [2] -list -> lists all files in directory.'
              f'\n| [3] -exit -> exit the program entirely.'
              f'\n╰ [4] -read -> re-read the current file.')
        return

    @staticmethod
    def help_file_command(*args):
         print(f'{w}{b}>> {u}File Help page:{e}'
              f'\n╭ [1] -help -> brings up a list of commands.'
              f'\n| [2] -list -> lists all files in directory.'
              f'\n| [3] -exit -> exit the current subsection.'
              f'\n| [4] -copy -> alone, copies email & password. Chained with "user", "pass", or "app" for respective copies.'
              f'\n|  ↪   ex: -copy app_name, -copy app_name user, -copy app_name pass, -copy app_name app'
              f'\n╰ [5] -read -> re-read the current file.')

    @staticmethod
    def exit_command(userInput, _):
        if len(userInput) > 1:
            return error_handler.error_catcher(3)
        return True

    @staticmethod
    def read_command(userInput, directory):
        if len(userInput) >= 3:
            return error_handler.error_catcher(3)
        try:
            read_files(userInput[1], directory)
        except IndexError:
            return error_handler.error_catcher(2)
        except FileNotFoundError:
            return error_handler.error_catcher(1, userInput[1])  # If file is not found.

    @staticmethod
    def copy_command(userInput, directory):
        test_file = 'C:\\Users\\Modesto\\Downloads\\KeyKrypt - v2.0\\Credentials\\OW_test.txt'
        try:
            # cmd_2, app_name, user_pass_or_app = locate_data()
            scan_function(userInput, test_file, directory)
        except IndexError:
            print(f'{Color.RED}{Color.BOLD}>> ERROR: {Color.END}{Color.RED}Command isn\'t valid, no passed arguments.'
                  f'\n     ↪ Type "-help" for commands!{Color.END}')
            return