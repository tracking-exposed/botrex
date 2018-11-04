import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib"))

from createGraph import createGraph, timeSetting
from fetchData import getBasic

# try to call createGraph
createGraph('impressions', getBasic(), timeSetting('week'))