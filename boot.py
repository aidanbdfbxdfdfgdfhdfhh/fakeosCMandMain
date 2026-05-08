from pathlib import Path
import subprocess
import sys
import json



with open("info.json", "r") as f:
    info = json.load(f)

BootAble = []
boot = "BootMenu: "

def get_bootable_files(folder_path,btlist):
    path = Path(folder_path)
    # Iterate through all .py files and grab their names
    for file in path.glob("*.py"):
        btlist.append(file.name)

# Usage

# Try USB first
get_bootable_files(info["USB"], BootAble)

# If USB was empty, try the Boot folder
if not BootAble: # This is the same as if BootAble == []
    get_bootable_files(info["Boot"], BootAble) # Add files directly to BootAble

# Now print whatever we found (either USB or Boot)
for key in BootAble:
    print(key)


while True:
    user = input(boot)
    if user in BootAble:
        # Start the next file
        subprocess.Popen([sys.executable, user])

        # Close the current file cleanly


        