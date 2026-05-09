import shutil
import subprocess
import shutil
import json
import requests
from pathlib import Path
import shlex

import os

def clear(): # This command needs 0 arguments
    os.system('cls' if os.name == 'nt' else 'clear')

clear()



# 1. Configuration - Replace these with your actual details
USERNAME = "aidanbdfbxdfdfgdfhdfhh"
REPO = "fakeosCMandMain"
BRANCH = "main" # or "master"
FILES = ["main.py", "cm.py", "boot.py"] # List your 3 file names exactly

# 2. Base Raw URL
BASE_URL = f"https://raw.githubusercontent.com/{USERNAME}/{REPO}/{BRANCH}/"

# 3. Download each file
current_dir = Path(__file__).parent
"""
for filename in FILES:
    print(f"Downloading {filename}...")
    try:
        response = requests.get(BASE_URL + filename)
        response.raise_for_status() # Check if download was successful
        
        with open(current_dir / filename, "wb") as f:
            f.write(response.content)
        print(f"Successfully saved {filename}")
        
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
"""
print("\nAll tasks finished!")



from colorama import Fore, Back, Style, init
init(autoreset=True, convert=True, strip=False)

from cm import commands,cl,get_display_path







def prompt():
    print(root, end="")
    return input()

username = ""
pw = ""
pw2 = ""
cf = ""
il = ""




info = {"username": "", "password": "","Boot":"","BOOTSCAN":""}

def user():
    print("enter your username")
    username = input("root@USER$")
    info["username"] = username
    with open(f"{il}info.json", "w") as f:
        json.dump(info, f)


    with open(f"{il}info.json", "w") as f:
        json.dump(info, f)
def boot():
    print("enter your boot were you install you os to same as il directroy needs to be a full dir")
    boot = input("root@BOOT$")
    info["Boot"] = boot

    with open(f"{il}info.json", "w") as f:
        json.dump(info, f)


def password():
    autologgin = input("press y for a password or n for no password: ").lower()   

    if autologgin == "n":
        return
    elif autologgin == "y":
        print("enter Password")
        pw = input("root@PW$ ")
        print("again must mathc")
        pw2 = input("root@PW$ ")
        if pw == pw2:
            info["password"] = pw
            with open(f"{il}/info.json", "w") as f:
                json.dump(info, f)
        else:
            print("They DO not match Try again")
            return None

def installLoca(il):
    print("must Enter Correct folder location eg:destination_folder/aidan")
    il = input("root@IL$ ")
    return il

def viewIL(il):
    print(il)

def install(il):
    shutil.copy2('main.py', f"{il}/main.py")
    shutil.copy2('cm.py', f"{il}/cm.py")

    with open(f"{il}/info.json", "w") as f:
        json.dump(info, f)

    print("Install Complete")
def inBOOT():
    shutil.copy2('boot.py', f"{info['Boot']}/boot.py")
    shutil.copy2('info.json', f"{info['Boot']}/info.json")

def helpIN():
    print("""
set password = PW
set username = UN
set Install Location = IL
install = IN
set Boot installe location = BOOT
install Boot = InBOOT
set Boot Scan Loaction = BTS
pwd is good command

"""
    )


def bts():
    print("enter your boot were you install you os to same as il directroy needs to be a full dir")
    boot = input("root@BOOT$")
    info["BOOTSCAN"] = boot

    with open(f"{il}info.json", "w") as f:
        json.dump(info, f)


while True:





    cd = get_display_path()
    root = f"{Fore.GREEN}root@fakeOs{cd}${Style.RESET_ALL} "
    user_input = shlex.split(prompt())
    if not user_input: continue # Handle empty Enter key
    instalCheck = True


    g = cl(user_input,instalCheck)
    if g == False:
        if user_input == ['UN']:
            user()

        elif user_input == ['PW']:
            password()

        elif user_input == ['IL']:
            il = installLoca(il)

        elif user_input == ['IN']:
            install(il)
        elif user_input == ['BOOT']:
            boot()
        elif user_input == ['InBOOT']:
            inBOOT()
        elif user_input == ['BTS']:
            bts()

        elif user_input == ['helpIn']:
            helpIN()
    



        else:
            print(f"Command '{user_input}' not a install Command.")


        