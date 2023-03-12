import discord
import dotenv
import os
import random
import time

dotenv.load_dotenv()

if __name__ == '__main__':
    while True:
        time.sleep(int(os.getenv("INTERVAL")))
        files = [f for f in os.listdir("./data") if ".txt" not in f]
        random.shuffle(files)
        with open("./data/" + files[0], "rb") as image_file:
            discord.set_profile_picture(auth_token=os.getenv("TOKEN"), image=image_file.read())
