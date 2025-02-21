"""MODULE file_operations.py keeps all file operations in safe, working order."""
import os
import time
import keyboard
import pyperclip
import error_handler
from utilities import *

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
    """FUNCTION read_files() displays the content of the file matching userInputFileName."""
    credentialsArray, _ = refresh_files(directory)  # Updates credentialsArray
    if not userInputFileName.strip():  # Ensures the userInput[1] isn't empty.
        raise IndexError
    if len(userInputFileName) > 1 and '.txt' not in userInputFileName:  # Add ".txt" if not present for search.
        userInputFileName += '.txt'
    for filePath in credentialsArray:
        if os.path.basename(filePath) == userInputFileName:  # Exact match
            with open(filePath, encoding='utf-8') as f:
                print(f'\n{w}{b}{u}{userInputFileName}{e}\n{f.read()}') # Prints file name on top and file content(s).
                return # Leaves the loop if condition is met (on top).
    raise FileNotFoundError  # If no file matches

def scan_function(userInput, currentFile, directory):
    """FUNCTION scan_function() allows the user to copy whichever information they'd like such as app name,
    username, password, etc."""
    credentialsArray, _ = refresh_files(directory)
    if '.txt' not in currentFile:  # Add ".txt" if not present for search.
        currentFile += '.txt'
    if f'{directory}\\{currentFile}' not in credentialsArray:
        raise FileNotFoundError
    matches = None
    actions = { # Dictionary for actions depending on input.
        "app": lambda: copy_to_clipboard(matches[0], "app"),
        "user": lambda: copy_to_clipboard(matches[1], "email"),
        "email": lambda: copy_to_clipboard(matches[1], "email"),
        "pass": lambda: copy_to_clipboard(matches[2], "password")
    }
    with open(f'{directory}\\{currentFile}', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for j in range(0, len(lines), 4): # From the start of the file to the end of the file, skipping 4 lines...
            app = lines[j].strip()
            email = lines[j+1][2:].strip()
            password = lines[j+2][2:].strip()
            if app.startswith(userInput[1]):
                matches = (app, email, password)
                break # Exit if match is found.
            if not matches and userInput[1] in app:
                 matches = (app, email, password)  # Stores 'closest' match (if substring is found).

    if not (len(userInput) > 2 and userInput[2] in actions or len(userInput) == 2):
        return error_handler.error_catcher(4, userInput[2])
    if not matches:
        return error_handler.error_catcher(5, userInput[1])

    if len(userInput) > 2 and userInput[2] in actions: # Handles user input ("email", "password", "app", etc.)
        actions[userInput[2]]()
    elif len(userInput) == 2:
        copy_to_clipboard(matches[1], "email")
        detect_ctrl_v()
        time.sleep(0.02)
        copy_to_clipboard(matches[2], "password")

def detect_ctrl_v():
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('v'):
            return True

def copy_to_clipboard(value, label):
    pyperclip.copy(value)
    print(f'Copied {label}: "{value}" to clipboard!')