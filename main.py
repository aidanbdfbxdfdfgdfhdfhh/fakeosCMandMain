import shutil
import json
from cm import commands,clear,cl,get_display_path
clear()
import shlex
import os
import time
import traceback

from colorama import Fore, Back, Style, init
init(autoreset=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INFO_PATH = os.path.join(BASE_DIR, "info.json")

# safe load (prevents instant crash)
info = {}
try:
    with open(INFO_PATH, "r") as file:
        info = json.load(file)
except FileNotFoundError:
    print("info.json missing, Try the installer again")




def prompt():
    cd = get_display_path()
    root = f"{Fore.GREEN}{info["username"]}@fakeOs{cd}${Style.RESET_ALL} "

    print(root, end="")
    return input()

def login(logins):
    global info 
    user = input("Login: ")
    user_pw = input("Password: ")
    if user == info["username"]:
        if user_pw == info["password"]:
            print("Loging in")
            return True
        else:
            print("incorrect pw")
            return False
    else:
        print("incorrect username")
        return False

logins = False


# -------------------------
# MAIN LOOP (your code kept)
# -------------------------
def run():
    

    global logins

    while logins == False:
        logins = login(logins)

    while True:
        
        user_input = shlex.split(prompt())
        if not user_input:
            continue
        instalCheck = False
        cl(user_input, instalCheck)


# -------------------------
# AUTO RESTART WRAPPER
# -------------------------
while True:
    try:
        run()

    except Exception:
        logins = False
        print("\nWe ran into an error, restarting...\n")
        print(traceback.format_exc())
        time.sleep(2)
        