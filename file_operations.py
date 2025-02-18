"""MODULE file_operations.py keeps all file operations in safe, working order."""
import os
import error_handler
from utilities import Color
b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE # Terminal color format.

def locate_directory():
    """FUNCTION locate_directory() is a one-time use function. Finds the locally saved credentials folder (dir)."""
    savedFileLocation = os.path.join(os.getcwd(), 'settings.txt')
    with open(savedFileLocation, 'r', encoding='utf-8') as f:
        directory = f.readline().replace('Credentials Directory: ', '').replace('\\', '/')[:-1]
    return directory

def refresh_files(directory):
    """FUNCTION refresh_files() refreshes the known directory contents to ensure up-to-date data."""
    directoryLen = len(os.listdir(directory))
    credentialsArray = [] * directoryLen
    for fileName in os.listdir(directory):
        credentialsArray.append(os.path.join(directory, fileName))
    return credentialsArray, directoryLen

def display_files(directory):
    """FUNCTION validate_files() goes through the directory (credentials folder) and prints if items present are valid
    or not. It will also print what items it is referring to"""
    credentialsArray, directoryLen = refresh_files(directory) # Double-checks if the credentials folder has been tampered with or not.
    credentialsValid = 0
    print(f'{w}{b}>> {u}Directory list page:{e}')
    for fileName in os.listdir(directory):
        f = os.path.join(directory, fileName)
        if os.path.isfile(f) and f.endswith('.txt'):
            print(f'{g}{b}[✔] | {e}"{fileName}" - {b}Valid!{e}')
            credentialsValid += 1
        else:
            print(f'{r}{b}[✖] | {e}"{fileName}" - {b}ISN\'T Valid!{e}')
    print(f'Total files present: {directoryLen} | Text files present: {credentialsValid}')
    return directory, credentialsArray, directoryLen

def read_files(userInputFileName, directory):
    """Displays the content of the file matching userInputFileName."""
    credentialsArray, _ = refresh_files(directory)  # Updates credentialsArray
    if not userInputFileName.strip():  # Ensures the userInput[1] isn't empty.
        raise FileNotFoundError
    for filePath in credentialsArray:
        if os.path.basename(filePath) == userInputFileName:  # Exact match
            with open(filePath, encoding='utf-8') as f:
                print(f'\n{w}{b}{u}{userInputFileName}{e}\n{f.read()}') # Prints file name on top and file content(s).
                return # Leaves the loop if condition is met (on top).
    raise FileNotFoundError  # If no file matches