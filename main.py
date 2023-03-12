import discord
import dotenv
import os
import random
import time
from rich import print

dotenv.load_dotenv()

if __name__ == '__main__':
    while True:
        print(f"Waiting {os.getenv('INTERVAL')} seconds")
        time.sleep(int(os.getenv("INTERVAL")))
        files = [f for f in os.listdir("./data") if f.split(".")[-1] in
                 (".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG")]

        if not len(files):
            print("No images found. ")
            continue

        random.shuffle(files)
        with open("./data/" + files[0], "rb") as image_file:
            print(f"Setting profile picture to: {files[0]}")
            response = discord.set_profile_picture(auth_token=os.getenv("TOKEN"), image=image_file.read())
            print("[yellow bold]--- DISCORD API RESPONSE START ---")
            print(f"Status Code: {response.status_code}", response.json())
            print("[yellow bold]--- DISCORD API RESPONSE END ---")
