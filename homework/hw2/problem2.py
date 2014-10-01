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
pp = pprint.PrettyPrinter(indent=4)

novemberFirst = dt.datetime.strptime("2012-11-01", "%Y-%m-%d") 
novemberLast = dt.datetime.strptime("2012-11-30", "%Y-%m-%d") 

startupinfo = None
if os.name == "nt":
    startupinfo = subprocess.STARTUPINFO()

elections = pd.DataFrame.from_csv("2012-general-election-romney-vs-obama.csv")

# pp.pprint(elections.head())

convert = lambda x: dt.datetime.strptime(x, "%Y-%m-%d")
inNovember = lambda x: 1 if x <= novemberLast and x >= novemberFirst else 0
date_time = elections["Start Date"].apply(convert)
elections["Start Date"] = date_time
inNovember = elections[elections["Start Date"] >= novemberFirst]
pp.pprint(inNovember.count())
med = inNovember["Number of Observations"].median()
pp.pprint(med)

samp = np.random.binomial(med, .53)

samps = []
for i in xrange(0,1000):
    samp = np.random.binomial(med, .53)
    samps.append(samp/float(med))
npSamps = np.asarray(samps)

plt.hist(map(lambda x: x*100,npSamps))
# plt.show()

npSamps.std()

means = []
for i in xrange(0,1000):
    generation = []
    for j in xrange(0,inNovember.count()[0]):
        generation.append(np.random.binomial(med, .53)/float(med))
    means.append(np.mean(np.array(generation)))

plt.hist(map(lambda x: x*100,means))
plt.show()










