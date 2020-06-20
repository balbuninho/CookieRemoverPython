import os
import sys

"""
Global Variables with paths to cookies files 
"""

path_gc = r'C:\Users\User\AppData\Local\Google\Chrome\User Data\Default\Cookies'
path_ff = r'C:\Users\User\AppData\Roaming\Mozilla\Firefox\Profiles\a79ram0e.default'



def remove_file(path):

    try:

        if os.path.exists(path) is True:  # remove file if exists
            os.remove(path)
            print('\033[92m'+'File has been removed :)'+'\033[0m')

        elif os.path.exists(path) is False:
            print('\033[93m' + 'File not found :('+'\033[0m')
        else:
            print('\033[93m' + 'Unexpected Error' + '\033[0m')
    except PermissionError:
        print('\033[93m' + 'Permission Denied' + '\033[0m')


if __name__ == "__main__":
    os.system('cls')  # Windows bug fix with color text printing
    remove_file(path_gc)
    remove_file(path_ff)
    sys.exit()