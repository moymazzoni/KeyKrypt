from file_operations import display_files, read_files

class GlobalCommands: # Hosts all commands.
    def __init__(self):
        pass

    @staticmethod
    def list_command():
        display_files(directory)
        return

    @staticmethod
    def help_command():
        print(f'{Color.BOLD}{Color.UNDERLINE}Selection Help page:{Color.END}'
              f'\n╭ [1] -help -> brings up a list of commands.'
              f'\n| [2] -list -> lists all files in directory.'
              f'\n| [3] -exit -> exit the program entirely.'
              f'\n╰ [x] ADD MORE LATER!')
        return

    @staticmethod
    def help_file_command():
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
    def read_command(cmd, directory):
        read_files(cmd, directory)