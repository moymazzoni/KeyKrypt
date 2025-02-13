"""MODULE file_operations.py keeps all file operations in safe, working order."""
import os

def locate_directory():
    print('find the directory in \'settings.txt\'.')
    credentials_array = os.path.join(os.getcwd(), 'settings.txt')
    return credentials_array

def check_files(credentials_array):
    print('check the directory and locate files.')