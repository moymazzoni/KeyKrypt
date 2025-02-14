"""MODULE file_operations.py keeps all file operations in safe, working order."""
import os
from utilities import Color
b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE # Terminal color format.


def locate_directory():
    """FUNCTION locate_directory() is a one-time use function. Finds the locally saved credentials folder (dir)."""
    saved_file_location = os.path.join(os.getcwd(), 'settings.txt')
    with open(saved_file_location, 'r', encoding='utf-8') as f:
        directory = f.readline().replace('Credentials Directory: ', '').replace('\\', '/')[:-1]
    return directory

def refresh_files(directory):
    """FUNCTION refresh_files() refreshes the known directory contents to ensure up-to-date data."""
    directory_len = len(os.listdir(directory))
    credentials_array = [] * directory_len
    for filename in os.listdir(directory):
        credentials_array.append(os.path.join(directory, filename))
    return credentials_array, directory_len

def display_files(directory, credentials_array, directory_len):
    """FUNCTION validate_files() goes through the directory (credentials folder) and prints if items present are valid
    or not. It will also print what items it is referring to"""
    refresh_files(directory) # Double-checks if the credentials folder has been tampered with or not.
    credentials_valid = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and f.endswith('.txt'):
            print(f'{g}{Color.BOLD}[✔] | {e}"{filename}" - {b}Valid!{e}')
            credentials_valid += 1
        else:
            print(f'{r}{b}[✖] | {e}"{filename}" - {b}ISN\'T Valid!{e}')
    print(f'Total files present: {directory_len} | Text files present: {credentials_valid}')
    return directory, credentials_array, directory_len

def read_files():
    print()
