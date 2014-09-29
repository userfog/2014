import requests
import pandas as pd
import zipfile
import pprint
from StringIO import StringIO
pp = pprint.PrettyPrinter(indent=4)

# r = requests.get("http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip")

# if r.status_code != 200:
#     print "Unable to get files"
#     exit(0)

# zf = zipfile.ZipFile(StringIO(r.content), "r")
path = r'C:\Users\Zachary\SkyDrive\School\Fall2014\cs109\2014\scraps\lahman-csv_2014-02-14.zip'

zf = zipfile.ZipFile(path, "r")
salaries_df = pd.read_csv(StringIO(zf.open("Salaries.csv", "rU").read()))
teams_df = pd.read_csv(StringIO(zf.open("Teams.csv", "rU").read()))
# print salaries_df.head()
# print teams_df.head()

 
# new_df = pd.merge(salaries_df, teams_df, left_on=["yearID", "teamID"], right_on=["yearID", "teamID"])

# print new_df.groupby(["teamID", "yearID"]).sum().head()
# summary_salaries = salaries_df.groupby(["teamID", "yearID"]).sum()
# wins_teams_years_salaries_df = pd.merge(summary_salaries, teams_df, left_on=["yearID", "teamID"], right_on=["teamID", "yearID"])
# wins_teams_years_salaries_df.head()

new_df = pd.merge(salaries_df, teams_df, left_on=["yearID", "teamID"], right_on=["yearID", "teamID"])
teams_years = new_df.groupby(["teamID", "yearID"]).sum()
print teams_years.head()




