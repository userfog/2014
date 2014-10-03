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
import calendar as cl
import StringIO
pp = pprint.PrettyPrinter(indent=4)

def build_frame(url):
    """
    Returns a pandas DataFrame object containing
    the data returned from the given url
    """
    source = requests.get(url).text
    
    # Use StringIO because pd.DataFrame.from_csv requires .read() method
    s = StringIO.StringIO(source)
    
    return pd.DataFrame.from_csv(s, index_col=None).convert_objects(
            convert_dates="coerce", convert_numeric=True)

url_str = "http://elections.huffingtonpost.com/pollster/api/charts/?topic=2014-senate"

election_urls = [election['url'] + '.csv' for election in requests.get(url_str).json()]
pp.pprint(election_urls)

# Makes a dictionary of pandas DataFrames keyed on election string.
dfs = dict((election.split("/")[-1][:-4], build_frame(election)) for election in election_urls)

pp.pprint(dfs["2014-kentucky-senate-mcconnell-vs-grimes"].head())

first_name = re.compile("senate-(.*?)-vs")
second_name = re.compile("vs-(.*)")

for key in dfs:
    if "kansas" in key:
        continue
    print key
    first_candidate = first_name.search(key)
    second_candidate = second_name.search(key)
    if not first_candidate or not second_candidate:
        continue

    name1 = first_candidate.group(1).title()
    name2 = second_candidate.group(1).title()
    indicies = set([0,2])
    if name1.startswith('Mcc') or name1.startswith('Mcf'):
        name1 = "".join(c.upper() if i in indicies else c for i, c in enumerate(name1))
    if name2.startswith('Mcc') or name2.startswith('Mcf'):
        name2 = "".join(c.upper() if i in indicies else c for i, c in enumerate(name2))
    
    dfs[key]["Diff"] = dfs[key][name1] - dfs[key][name2]
    m = dfs[key]["Number of Observations"].median()
    # pp.pprint(dfs[key].head())
    # pp.pprint(dfs[key]["Diff"].head())
    lst = []
    pred = []
    for i in xrange(1000):
        for j in xrange(int(m)):
            sample = np.random.choice(dfs[key]["Diff"])
            lst.append(sample)
    pred.append(("Prediction %s: Expected Difference: %f Std Error: %f" % ((name1 + " - " + name2), np.array(lst).mean(), np.array(lst).std())))


    with open("Prediction100.txt", "a") as out:
        for el in pred:
            out.write(el + "\n")
    




