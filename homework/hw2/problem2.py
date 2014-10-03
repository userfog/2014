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
N = inNovember["Number of Observations"].median()
pp.pprint(N)

samp = np.random.binomial(N, .53)

samps = []
for i in xrange(0,1000):
    samp = np.random.binomial(N, .53)
    samps.append(samp/float(N))
npSamps = np.asarray(samps)

# plt.hist(map(lambda x: x*100,npSamps))
# plt.show()

one_trial_std = npSamps.std()

means = []
stds = []
for i in xrange(0,1000):
    generation = []
    for j in xrange(0,inNovember.count()[0]):
        generation.append(np.random.binomial(N, .53)/float(N))
    means.append(np.mean(np.array(generation)))
    stds.append(np.array(generation).std())

# plt.hist(map(lambda x: x*100,means))
# plt.show()
nineteen_trial_std = np.array(means).std()

# The ratio of the standard errors is reduced by a factor of the square root
# of the number of samples per trial.

stds_100 = map(lambda x: x*100, stds)

# plt.hist(map(lambda x: x*100, stds))

actual_std = inNovember["Obama"].std()

pp.pprint(actual_std)
pp.pprint(np.array(stds_100).mean())

pp.pprint(actual_std/np.array(stds_100).mean())










	







