import sys
import os
from pathlib import Path
import json
import shutil
import subprocess




def nano(filename):
    os.system(f"nano {filename}")

def ls(folder_path="."):
    try:
        # This lists everything (files and directories) in the path
        items = os.listdir(folder_path)
        print(items)
    except FileNotFoundError:
        print("FileNotFoundError")


def clear(): # This command needs 0 arguments
    os.system('cls' if os.name == 'nt' else 'clear')

def mkdir(folder_path="."):
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    print("Success")

def rm(path_name=""):
    if path_name == "":
        print("Nothing to remove")
        return

    path = Path(path_name)

    if not path.exists():
        print(f"Error: '{path_name}' not found.")
        return

    y = input(f"Are you sure you want to delete {path_name}? (y/n): ").lower()
    
    if y == "y":
        if path.is_file():
            path.unlink()
            print(f"File '{path_name}' deleted.")
        elif path.is_dir():
            shutil.rmtree(path)
            print(f"Folder '{path_name}' and all contents deleted.")
    else:
        print("Deletion cancelled.")

def cl(user_input,instalCheck):

    
    cm = user_input[0]    # The first word is the command name
    args = user_input[1:] # Everything else is a list of arguments


    if cm in commands:
        
        func = commands[cm]
        # Check if the command actually needs arguments
        if cm == "clear":
            func()
        elif cm == "shutdown":
            func()
        elif cm == "pwd":
            func()    
        elif cm == "help":
            help()   
        else:
            path = args[0] if args else "."
            func(path)
        return True

    else:
        if instalCheck == False:
            print(f"Command '{cm}' not found.")
        else:
            return False
        
def help():
    print(

"""
list = ls
make folder = mkdir foldername
remove a folder = rm folrder
to clear the ternale = clear
to make files or edit them  = nano
change dir = cd
python egfilename.py to run python files


"""

)

BASE_DIR = Path(__file__).parent.parent.resolve() 

def get_display_path():
    current = Path.cwd()
    
    # Calculate the path relative to your root
    relative = current.relative_to(BASE_DIR)
    
    # If the user is AT the root, relative will be "."
    # We can replace it with "~" or "/" for a better look
    if str(relative) == ".":
        return "~"
    return f"~/{relative}"


def pwd(path_unused=None):
    # This prints the exact absolute path you are currently in
    print(os.getcwd())


def cd(target_path):
    # 1. Calculate what the NEW path would be
    current_dir = Path.cwd()
    new_path = (current_dir / target_path).resolve()

    # 2. Check if the new path starts with the BASE_DIR
    if BASE_DIR in new_path.parents or new_path == BASE_DIR:
        os.chdir(new_path)
    else:
        print("Access Denied: You cannot leave the fake OS root!")

def shutdown():
    sys.exit()

def python(pyfile):
    try:
        # Replace 'another_file.py' with your target filename
        subprocess.run(["python", pyfile])
    except KeyboardInterrupt:
        # This catches Ctrl+C if it bubbles up to the parent script
        print("\nInterrupted! Returning to the previous file.")
# STORE ONLY THE FUNCTION NAMES
commands = {
    "ls": ls,
    "clear": clear,
    "mkdir": mkdir,
    "rm":rm,
    "help":help,
    "cd":cd,
    "shutdown":shutdown,
    "nano":nano,
    "pwd": pwd,
    "python":python
}