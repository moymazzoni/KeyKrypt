"""MODULE terminal_commands.py contains all the commands that ties back to file_operations.py or its own functions."""
import error_handler
from file_operations import display_files, read_files, scan_function
from utilities import *

class GlobalCommands: # Hosts all commands.
    """CLASS GlobalCommands contains all commands in a dictionary and the functions for the correlating command."""
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

    def process_command(self, userInput, directory, terminalKey, currentFile):
        """FUNCTION process_command() is where the userInput goes in and gets sent to the appropriate function."""
        userInput = list(filter(None, userInput.split(' ')))  # Chops up the text so only words are passed as args.
        try:
            action = self.commands.get(userInput[0], lambda *_: error_handler.error_catcher(0))
            isAction = action(userInput, directory, terminalKey, currentFile)  # Pass terminalKey dynamically
            if isAction == 'exit':  # If exit command was input, exit.
                return 'exit'
            if isAction == 'read': # If read command was input, read.
                return 'read'
        except (TypeError, IndexError):  # Catches empty inputs or invalid ones
            error_handler.error_catcher(0)
        return

    @staticmethod
    def list_command(userInput, directory, *args):
        _ = args # Unused value but must be passed in function.
        if len(userInput) > 1:
            return error_handler.error_catcher(3)
        return display_files(directory)

    @staticmethod
    def help_command(userInput, _, terminalKey, *args):
        _ = args
        if len(userInput) > 1:
            return error_handler.error_catcher(3)
        if terminalKey == 'terminal_2':
            print(f'{w}{b}>> {u}File Help page:{e}'
                  f'\n╭ [1] -help -> brings up a list of commands.'
                  f'\n| [2] -list -> lists all files in directory.'
                  f'\n| [3] -read -> re-read the current file.'
                  f'\n| [4] -copy -> alone, copies email & password. Chained with "user", "pass", or "app" for respective copies.'
                  f'\n|  ↪   ex: "-copy app_name", "-copy app_name user", "-copy app_name pass", "-copy app_name app".'
                  f'\n| [5] -exit -> exit the current subsection.'
                  f'\n╰ {r}[!]{e} Invalid files may still be able to be read, but don\'t expect commands to function!'
                  f'\n   ↪   It is recommended to reformat the file to conform with file standards.')
            return
        else:
            print(f'{w}{b}>> {u}Selection Help page:{e}'
                  f'\n╭ [1] -help -> brings up a list of commands.'
                  f'\n| [2] -list -> lists all files in directory.'
                  f'\n| [3] -read -> prints content(s) of file. Chained with file name as argument.'
                  f'\n|  ↪   ex: "-read personalAccounts_file", "-r emailAccounts".'
                  f'\n| [4] -exit -> exit the program entirely.'
                  f'\n╰ {r}[!]{e} Invalid files may still be able to be read, but don\'t expect commands to function!'
                  f'\n   ↪   It is recommended to reformat the file to conform with file standards.')
            return

    @staticmethod
    def exit_command(userInput, *args):
        _ = args
        if len(userInput) > 1:
            return error_handler.error_catcher(3)
        return 'exit'

    @staticmethod
    def read_command(userInput, directory, terminalKey, currentFile):
        if terminalKey == 'terminal_2': # In terminal_2
            if len(userInput) >= 2:
                return error_handler.error_catcher(3)
            try:
                read_files(currentFile, directory)
                return print(f'{w}{b}>> ^^ Re-read document ^^{e}')
            except FileNotFoundError:
                error_handler.error_catcher(7, currentFile)
                return 'exit'
        if len(userInput) >= 3: # In terminal (1)
            return error_handler.error_catcher(3)
        try:
            result = read_files(userInput[1], directory)
            if result == 'invalid':
                return
            else:
                return 'read'
        except IndexError:
            return error_handler.error_catcher(2)
        except FileNotFoundError:
            return error_handler.error_catcher(1, userInput[1])  # If file is not found.

    @staticmethod
    def copy_command(userInput, directory, terminalKey, currentFile):
        if terminalKey == 'terminal':
            return error_handler.error_catcher(0)
        else:
            try:
                # cmd_2, app_name, user_pass_or_app = locate_data()
                scan_function(userInput, currentFile, directory)
            except IndexError:
                return error_handler.error_catcher(2)
            except FileNotFoundError:
                error_handler.error_catcher(6, currentFile)
                return 'exit'