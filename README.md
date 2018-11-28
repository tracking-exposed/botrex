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
    
### Edit your configuration files

they have this format (see example in config/):

    # for config/general.conf
    --token abc123:abc123123 # See below on how to obtain a token throught the BotFather
    
    # for config/channelupdate.conf
    --timeframe 24 # integer of number of hours to get the stats for
    --channel_id (@channel_name or -1001231231231) # Name of the channel or ID (in case it is private), could be obtained by using      Telegram Plus or cli.


To create a bot and get a **token**, just talk to the **BotFather**: https://telegram.me/botfather. Channel ID is the ID of your channel, can be '@channel'.

## Run the script:

    python3 botrex.py


