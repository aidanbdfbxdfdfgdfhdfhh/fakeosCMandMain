import requests
from pathlib import Path

def pacman(FILES):

    # 1. Configuration - Replace these with your actual details
    USERNAME = "aidanbdfbxdfdfgdfhdfhh"
    REPO = "fakeosCMandMain"
    BRANCH = "main" # or "master"


    # 2. Base Raw URL
    BASE_URL = f"https://raw.githubusercontent.com/{USERNAME}/{REPO}/{BRANCH}/"

    # 3. Download each file
    current_dir = Path(__file__).parent

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

    print("\nAll tasks finished!")