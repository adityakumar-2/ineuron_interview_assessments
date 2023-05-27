# importing irequired libraries
import urllib.request
import json 
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt

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



# Get all the overall ratings for each season and using plots compare the ratings for all the seasons, like season 1 ratings, season 2, and so on.
print("Insight: Get all the overall ratings for each season and using plots compare the ratings for all the seasons, like season 1 ratings, season 2, and so on.\n")
var = []
for i in set(df1["season"]):
    var.append(df1["average rating"][df1["season"] == i].mean())
xpoints = [i+1 for i in range(len(var))]
ypoints = var
plt.xticks(xpoints)
plt.xlabel("season")
plt.ylabel("season wise overall rating")
plt.plot(xpoints, ypoints, marker = "o")
plt.show(block = False)
print("\n")

# Get all the episode names, whose average rating is more than 8 for every season
print("Insight: Get all the episode names, whose average rating is more than 8 for every season\n")
var = []
for i in range(len(df1["name"])):
    if df1["average rating"].iloc[i] > 8:
        var.append(df1["name"].iloc[i])
print(f"There are total {len(var)} such episodes and are listed below:\n")
print(var)
print("\n")

# Get all the episode names that aired before May 2019
print("Insight: Get all the episode names that aired before May 2019\n")
var = []
for i in range(len(df1["name"])):
    if df1["airdate"].iloc[i].year < 2019 or (df1["airdate"].iloc[i].month < 5 and df1["airdate"].iloc[i].year == 2019):
        var.append(df1["name"].iloc[i])
print(f"There are total {len(var)} such episodes and are listed below:\n")
print(var)
print("\n")

# Get the episode name from each season with the highest and lowest rating
print("Insight: Get the episode name from each season with the highest and lowest rating\n")
var = pd.Series(dtype = object)
new_df = pd.DataFrame()
for i in set(df1["season"]):
    new_df = df1[["name", "average rating"]][df1["season"] == i]
    var = pd.concat([var,new_df["name"][new_df["average rating"] == new_df["average rating"].max()]])
    var = pd.concat([var,new_df["name"][new_df["average rating"] == new_df["average rating"].min()]])
var = var.to_list()
print(f"There are total {len(var)} such episodes and are listed below:\n")
print(var)
print("\n")


# Get the summary for the most popular ( ratings ) episode in every season
print("Insight: Get the summary for the most popular ( ratings ) episode in every season\n")
var = pd.Series(dtype = object)
new_df = pd.DataFrame()
for i in set(df1["season"]):
    new_df = df1[["summary", "average rating"]][df1["season"] == i]
    var = pd.concat([var,new_df["summary"][new_df["average rating"] == new_df["average rating"].max()]])
var = var.to_list()
print(f"There are total {len(var)} such episodes and their summary are listed below:\n")
print(var)
print("\n")