from telegram.ext import Updater, CommandHandler
import logging
import json
import fbtrex

# LOAD CONFIGURATION
#must be a json file containing two values: token and chat_id

with open('config.json', 'r') as f:
    config = json.load(f)

# initialize telegram bot
updater = Updater(token=config['token'])
dispatcher = updater.dispatcher

#logging and error handling
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#define commands: handlers and callback functions

def stats(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text=fbtrex.GetData(args[0]))

stats_handler = CommandHandler('stats', stats, pass_args=True)
dispatcher.add_handler(stats_handler)

def chart(bot, update, args):
    bot.send_photo(chat_id=update.message.chat_id, photo=fbtrex.GetGraph(args[0], args[1]))

chart_handler = CommandHandler('chart', chart, pass_args=True)
dispatcher.add_handler(chart_handler)

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Welcome to the facebook.tracking.exposed bot!\nHere is a list of commands: \n\n/stats\nRequires argument: hours as number. (For example, \"/stats 24\" will return the last 24 hours.) \n\n/chart\nRequires two arguments: which statistic to plot (htmls, impressions, newsupporters, timelines,  visits) and what timeframe (day, week or month). (For example \"/chart htmls day\". \n\n/Help\nDisplays this help.')

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


#start the bot
updater.start_polling()
