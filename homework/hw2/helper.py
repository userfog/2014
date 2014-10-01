# special IPython command to prepare the notebook for matplotlib
# %matplotlib inline 
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

oct31 = dt.datetime.strptime("31/10/2002", "%d/%m/%Y")
LOCAL = True

def sinceOctober2002(date):
	# print date
	time = dt.datetime.strptime(date, "%m/%d/%y")
	delt = time - oct31
	return delt.days


class getDataFrame():
	def __init__(self, local, name):
		self.df = []
		if local:
			with open(name, "rU") as infile:
				self.df = pd.DataFrame.from_csv(infile)
		else:
			self.df = pd.DataFrame.from_csv(StringIO.StringIO(requests.get(name)))

startupinfo = None
if os.name == "nt":
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW


exprs_remote = "https://raw.githubusercontent.com/cs109/2014_data/master/exprs_GSE5859.csv"
smpl_remote = "https://raw.githubusercontent.com/cs109/2014_data/master/sampleinfo_GSE5859.csv"
exprs_local = "exprs_GSE5859.csv"
smpl_local = "sampleinfo_GSE5859.csv"

exprs_name = ""
smpl_name = ""

if LOCAL:
	exprs_name = exprs_local
	smpl_name = smpl_local
else:
	exprs_name = exprs
	smpl_name = smpl

#Problem 1a
exprs = getDataFrame(LOCAL,exprs_name).df
sampleinfo = getDataFrame(LOCAL,smpl_name).df
#Problem 1b
sampleinfo.sort(["filename"], inplace=True)
ordered = sorted(exprs.columns.tolist())
exprs = exprs[ordered]
#Problem 1c
sampleinfo["elapsedInDays"] = sampleinfo["date"].map(sinceOctober2002)
# pp.pprint(sampleinfo.head())
# Problem 1d
# part 1
sampleinfo = sampleinfo.reset_index()
sampleinfoCEU = sampleinfo[sampleinfo["ethnicity"].str.contains("CEU")]
pp.pprint(sampleinfoCEU.head())
#part 2
exprsCEU = pd.DataFrame()
for col in sampleinfoCEU["filename"]:
	exprsCEU[col] = exprs[col]

# part 3
(exprsCEU.columns == sampleinfoCEU["filename"]).all()
# part 4
# deviations = lambda x: np.fabs((x-x.mean())/x.std())
deviations = lambda x: (x-x.mean())
exprsCEU = exprsCEU.apply(deviations)
print exprsCEU.head()
# part 5
U, s, Vh = np.linalg.svd(exprsCEU)
V = Vh.T

# #part 5
plt.hist(V[:,0:1], bins=25)
plt.show()

# part 6
f, (ax1) = plt.subplots(ncols=1)
ax1.scatter(sampleinfoCEU["elapsedInDays"], V[:,0:1])
# f.tight_layout()
f.show()
x = raw_input()

# It looks like around the 200th day of the sample the results for the group
# stop being similar.

















