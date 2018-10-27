import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from io import BytesIO

def GetData(hours):
    data = requests.get("https://facebook.tracking.exposed/api/v1/stats/basic/1").json()

    s = (-(int(hours)))-1
    data = data[s:-1]

    visits = str(sum(item['visits'] for item in data))
    timelines = str(sum(item['timelines'] for item in data))
    newsupporters = str(sum(item['newsupporters'] for item in data))
    htmls = str(sum(item['htmls'] for item in data))
    impressions = str(sum(item['impressions'] for item in data))

    msg = 'Stats for last '+hours+' hours:\n\n{} visits\n{} timelines\n{} new supporters\n{} htmls\n{} impressions'.format(
        visits, timelines, newsupporters, htmls, impressions)

    return msg


def GetGraph(what, when):

    #set timeframe variables
    if when == 'day':
        floor = 'H'
        locator = matplotlib.dates.HourLocator(interval=2)
        formatter = matplotlib.dates.DateFormatter('%H:%m\n%d %b')
        start = (1 * -24) - 1
    elif when == 'week':
        floor = 'D'
        locator = matplotlib.dates.DayLocator(interval=1)
        formatter = matplotlib.dates.DateFormatter('%d\n%b')
        start = (7 * -24) - 1
    elif when == 'month':
        floor = 'D'
        locator = matplotlib.dates.DayLocator(interval=3)
        formatter = matplotlib.dates.DateFormatter('%d\n%b')
        start = (31 * -24) - 1

    # fetch json data from public API
    data = requests.get("https://facebook.tracking.exposed/api/v1/stats/basic/1"
                        ).json()
    # determine when in correct format and select data
    data = data[start:-1]

    # create pandas dataframe
    df = pd.DataFrame(data)
    # make it lighter straight away
    df = df[[what, 'start']]

    #format index as date (day)
    df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df['start'], format='%Y-%m-%d %H:%M:%S')))
    del df['start'] # it's useless now

    # aggregate all data to daily stats
    df.index = df.index.floor(floor)
    df = df.groupby(df.index).sum()

    # PLOT IT
    f, ax = plt.subplots(1, figsize=(10, 5))
    x = df.index
    ax.plot(x, df[what])
    ax.set_title(what)
    ax.grid(True)

    # Set major x ticks on Mondays.
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    # save in buffer as png and return it
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer
