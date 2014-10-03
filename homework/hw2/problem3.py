import os
import copy
import sys
import subprocess
import requests 
from StringIO import StringIO
import numpy as np
import pandas as pd # pandas
import matplotlib.pyplot as plt # module for plotting 
import zipfile
import StringIO
import datetime as dt # module for manipulating dates and times
import numpy.linalg as lin # module for performing linear algebra operations
import scipy
import pprint
import datetime as dt
import math
import re
import matplotlib.dates as mdates
pp = pprint.PrettyPrinter(indent=4)

startupinfo = None
if os.name == "nt":
    startupinfo = subprocess.STARTUPINFO()

elections = pd.DataFrame.from_csv("2012-general-election-romney-vs-obama.csv")

elections["Diff"] = elections["Obama"] - elections["Romney"]
convert = lambda x: dt.datetime.strptime(x, "%Y-%m-%d").date()
date = elections["Start Date"].apply(convert)
elections["Start Date"] = date
# https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib
five_days = elections[elections["Start Date"] >= dt.datetime.strptime("2012-11-1", "%Y-%m-%d").date()]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(np.array(five_days["Start Date"]), np.array(five_days["Diff"]), "ro")
plt.gcf().autofmt_xdate()
plt.show()
ten_days = elections[elections["Start Date"] >= dt.datetime.strptime("2012-11-1", "%Y-%m-%d").date()- dt.timedelta(days=5)]
ten_days = ten_days.reset_index()
# plotter = ten_days[["Pollster", "Diff"]]
# plotter.boxplot(by="Pollster", rot=45)
# plt.show()

ten_days = ten_days.groupby("Pollster")
ten_days = ten_days.mean()
print ten_days["Diff"].mean()