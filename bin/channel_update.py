import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib"))
from createText import createText
from fetchData import getBasic
from urllib.parse import urlencode
import urllib.request
import configargparse

p = configargparse.ArgParser(default_config_files=[os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/channelupdate.conf")), os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/general.conf"))])
p.add('-c', '--my-config', is_config_file=True, help='config file path')
p.add('-t', '--timeframe', required=True, help='timeframe in hours (integer) for the stats')
p.add('-i', '--channel_id', required=True, help='id or name of the channel')
p.add('-b', '--token', help='bot token', required=True)
args = p.parse_args()

timeframe = int(args.timeframe)
channel_id = args.channel_id
bot_id = args.token

def spam():
    url = "https://api.telegram.org/bot" + bot_id + "/sendMessage"
    args = {}
    args['chat_id'] = channel_id
    args['text'] = createText(timeframe, getBasic())
    post_data = urlencode(args)
    request = urllib.request.Request(url, bytearray(post_data, 'utf-8'))
    response = urllib.request.urlopen(request)

if __name__ == "__main__":
    spam()
