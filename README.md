# botrex
Telegram Bot for tracking.exposed

a python3 software


### Install system requirements (Debian/Ubuntu)

    sudo apt-get install git python3-venv python3-dev python3-tk
    
### Clone bottrex with git and move to that folder:

    git clone https://github.com/tracking-exposed/botrex.git && cd botrex

### Now create a virtual environment and activate it

    python3 -m venv venv && source venv/bin/activate

> If you want to deactivate it, just use the command 

    deactivate

### Install the requirements:

    python3 -m pip install -r requirements.txt
    
### Edit your configuration file

has this format (see example in config/):

    --token abc123:abc123123


To create a bot and get a **token**, just talk to the **BotFather**: https://telegram.me/botfather. Channel ID is the ID of your channel, can be '@channel'.

## Run the script:

    python3 botrex.py


