'''
Update function for the program
Usage:
    Just make changes
    PUSH THEM TO GITHUB
    To update, call python3 update.py
'''

# Imports
from os import getcwd, chdir
from subprocess import check_output, CalledProcessError

def main():
    directory = getcwd()
    parent_directory = directory.replace("/network", "")
    chdir(parent_directory)
    try:
        delete_directory = check_output(["rm", "-R", "network"])
        print("Deleted Directory")
        git_clone = check_output(["git", "clone", "https://github.com/ycao123/network"])
        print("Finished!")
        
    except CalledProcessError:
        print("Error: Bad Stuff Detected")
        exit(1)

    print(git_clone)

if __name__ == "__main__":
    main()
