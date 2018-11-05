import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from io import BytesIO

def timeSetting(tick):
    if tick == 'day':
        return {
            "granularity": tick,
            "floor": 'H',
            "interval": 2,
            "formatter": '%H:%m\n%d %b',
            "start": (1 * -24) - 1
         }
    if tick == 'week':
        return {
            "granularity": tick,
            "floor": 'D',
            "interval": 1,
            "formatter": '%d\n%b',
            "start": (7 * -24) - 1
         }
    if tick == 'month':
        return {
            "granularity": tick,
            "floor": 'D',
            "interval": 3,
            "formatter": '%d\n%b',
            "start": (31 * -24) - 1
         }

    raise Error("Invalid tick requested");

def createGraph(what, data, when):
    """
    @what is a string, used in the graph
    @data is a collection of data
    @when is an object, it can take three meanings (day,week,month)
        granularity: 'day' | 'week' | 'month'
        floor: H | D | D
        interval: <Int>
        formatter: <String>
        start: <Int>
    """
    print("createGraph: %s (%d object) %j", what,
          # data.length(),
          when)

    # determine when in correct format and select data
    data = data[when['start']:-1]

    # create pandas dataframe
    df = pd.DataFrame(data)
    # make it lighter straight away
    df = df[[what, 'start']]

    # format index as date (day)
    df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df['start'], format='%Y-%m-%d %H:%M:%S')))
    del df['start'] # it's useless now

    # aggregate all data to daily stats
    df.index = df.index.floor(when['floor'])
    df = df.groupby(df.index).sum()

    # plot it
    f, ax = plt.subplots(1, figsize=(10, 5))
    x = df.index
    ax.plot(x, df[what])
    ax.set_title(what)
    ax.grid(True)

    # set x ticks correctly

    if when['floor'] == 'H':
        ax.xaxis.set_major_locator(matplotlib.dates.HourLocator(interval=when['interval']))
    else:
        ax.xaxis.set_major_locator(matplotlib.dates.DayLocator(interval=when['interval']))

    ax.xaxis.set_major_formatter(
        matplotlib.dates.DateFormatter(when['formatter'])
    )

    # save in buffer as png and return it
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer
