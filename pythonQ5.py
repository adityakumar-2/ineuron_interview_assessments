# importing irequired libraries
import urllib.request
import json 
import pandas as pd
from datetime import datetime as dt

# downloading data and converting into dataframe
url = ' http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

df = pd.DataFrame(data["_embedded"]["episodes"])

# creating new dataframe df1 with only required columns in correct format
df1 = pd.DataFrame()
df1[["id"]] = pd.DataFrame(df[["id"]], dtype = "int")
df1[["url"]] = pd.DataFrame(df[["url"]], dtype = "str")
df1[["name"]] = pd.DataFrame(df[["name"]], dtype = "str")
df1[["season"]] = pd.DataFrame(df[["season"]], dtype = "int")
df1[["number"]] = pd.DataFrame(df[["number"]], dtype="int")
df1["type"] = pd.DataFrame(df[["type"]], dtype = "str")
df1["airdate"] = pd.to_datetime(df["airdate"])

# converting 24 hour time to 12 hour time format
new_time = []
for i in df["airtime"]:
    new_time.append(dt.strptime(i, "%H:%M").strftime("%I:%M %p"))

df1["airtime"]=pd.Series(new_time)

# adding runtime column to df1
df1["runtime"] = pd.DataFrame(df[["runtime"]], dtype = "float")

# adding average rating column in df1
avg_rating = []

for i in range(len(data["_embedded"]["episodes"])):
    avg_rating.append(data["_embedded"]["episodes"][i]["rating"]["average"])

df1["average rating"] = pd.Series(avg_rating, dtype = "float")

# adding summary column in df1 and removing HTML tags
new_summary = []
for i in df["summary"]:
    new_summary.append(i.strip("</p>"))
    
df1["summary"] = pd.DataFrame(new_summary, dtype = "str")

# adding medium image and original image link column in df1
med_image = []
org_image = []

for i in range(len(data["_embedded"]["episodes"])):
    med_image.append(data["_embedded"]["episodes"][i]["image"]["medium"])
    org_image.append(data["_embedded"]["episodes"][i]["image"]["medium"])

df1["medium image link"] = pd.Series(med_image)
df1["Original image link"] = pd.Series(org_image)

# Saving the file in CSV fomat without index
df1.to_csv("episode.csv", index = False)
