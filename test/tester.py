import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib"))
from pathlib import Path
from createGraph import createGraph, timeSetting
from createText import createText
from fetchData import getBasic

from telegram.ext import Updater, CommandHandler
import logging
import json


# load configuration
config_path = str(Path(os.path.join(os.path.dirname(os.path.dirname(__file__)))))+'/config/config.json'

with open(config_path, 'r') as f:
    config = json.load(f)

# initialize telegram bot
updater = Updater(token=config['token'])
dispatcher = updater.dispatcher

# logging and error handling
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# define commands: handlers and callback functions

def stats(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text=createText(args[0], getBasic()))

stats_handler = CommandHandler('stats', stats, pass_args=True)
dispatcher.add_handler(stats_handler)

def chart(bot, update, args):
    bot.send_photo(chat_id=update.message.chat_id, photo=createGraph(args[0], getBasic(), timeSetting(args[1])))

chart_handler = CommandHandler('chart', chart, pass_args=True)
dispatcher.add_handler(chart_handler)

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Welcome to the facebook.tracking.exposed bot!\nHere is a list of commands: \n\n/stats\nRequires argument: hours as number. (For example, \"/stats 24\" will return the last 24 hours.) \n\n/chart\nRequires two arguments: which statistic to plot (htmls, impressions, newsupporters, timelines,  visits) and what timeframe (day, week or month). (For example \"/chart htmls day\". \n\n/Help\nDisplays this help.')

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


# start the bot
updater.start_polling()
