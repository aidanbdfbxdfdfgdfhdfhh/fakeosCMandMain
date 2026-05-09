from pathlib import Path
import sys
import json
import os # Added for execv

with open("info.json", "r") as f:
    info = json.load(f)

BootAble = []
boot = "BootMenu: "

def get_bootable_files(folder_path, btlist):
    path = Path(folder_path)
    if path.exists(): # Safety check
        for file in path.glob("*.py"):
            btlist.append(file.name)

# Try BOOTSCAN first
get_bootable_files(info["BOOTSCAN"], BootAble)

# If BOOTSCAN was empty
if not BootAble:
    print(f"no os in {info["BOOTSCAN"]}")

# Print found options
for key in BootAble:
    print(key)

while True:
    user = input(boot)
    if user in BootAble:
        # 1. Determine the correct full path
        full_path = Path(info["BOOTSCAN"]) / user

        # 2. Replace current process with the new script
        # This fixes the EOFError by keeping the terminal connection
        os.execv(sys.executable, [sys.executable, str(full_path)])

