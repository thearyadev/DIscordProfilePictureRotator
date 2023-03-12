# Discord Profile Picture Rotator

A tool to automatically change your discord profile picture. Note: Your discord account may get banned. Use at your own risk.

## Installation and Usage
Note: These instructions require the following tools installed: git, docker, docker-compose
1. Get your discord token. Theres plenty of resources online on how to do this. 
2. Find some profile pictures you would like to use.
3. Run the command `git clone https://github.com/thearyadev/discordprofilepicturerotater` This will clone the repository to your local environment. 
4. CD into the project directory. `cd DiscordProfilePictureRotator`
5. Open `./docker-compose.yaml` in a text editor.
   In this file, read all the comments (all lines starting with a `#`) and add all the missing information.
6. Run the command `docker-compose up -d`

To stop the deployment, use the command `docker-compose down` in the project directory. You can then edit the `docker-compose.yaml` file. To redeploy, run `docker-compose up -d`