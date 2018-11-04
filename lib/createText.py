def createText(hours, data):
    s = -int(hours)-1
    data = data[s:-1]

    visits = str(sum(item['visits'] for item in data))
    timelines = str(sum(item['timelines'] for item in data))
    newsupporters = str(sum(item['newsupporters'] for item in data))
    htmls = str(sum(item['htmls'] for item in data))
    impressions = str(sum(item['impressions'] for item in data))

    msg = 'Stats for the last '+str(hours)+' hours:\n\n{} visits\n{} timelines\n{} new supporters\n{} htmls\n{} impressions'.format(
        visits, timelines, newsupporters, htmls, impressions)

    return msg
