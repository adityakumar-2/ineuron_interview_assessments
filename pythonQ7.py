# importing required libraries
import urllib.request
import json 
import pandas as pd

# reading data from provided URL
url = 'https://data.nasa.gov/resource/y77d-th95.json'
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())
    
# Converting data into a pandas dataframe
df = pd.DataFrame(data)

# Creating a new dataframe with desired column names and data types
df1 = pd.DataFrame()
df1[["Name of Earth Meteorite"]] = pd.DataFrame(df[["name"]], dtype = "str")
df1[["ID of Earth Meteorite"]] = pd.DataFrame(df[["id"]], dtype = "int")
df1[["nametype"]] = pd.DataFrame(df[["nametype"]], dtype = "str")
df1[["recclass"]] = pd.DataFrame(df[["recclass"]], dtype = "str")
df1[["Mass of Earth Meteorite"]] = pd.DataFrame(df[["mass"]], dtype="float")
df1["Year at which Earth Meteorite was hit"] = pd.to_datetime(df["year"], errors = 'coerce')
df1[["reclat"]] = pd.DataFrame(df[["reclat"]], dtype="float")
df1[["recclong"]] = pd.DataFrame(df[["reclong"]], dtype="float")

# Creating a list of integer coordiantes
df2 = df["geolocation"].apply(pd.Series)

# convering series into a list
df2["coordinates"].values.tolist()

# changing the data type of list to integer
a = []
for i in df2["coordinates"].values.tolist():
    if type(i) != list:
        a.append(i)
    else:
        a.append([int(x) for x in i])

# adding the list of integer coordinates to the dataframe
df1["point coordinates"] = pd.Series(a)


# Get all the Earth meteorites that fell before the year 2000
print("Insight: Get all the Earth meteorites that fell before the year 2000\n")
var = []
for i in range(len(df1["Name of Earth Meteorite"])):
    if df1["Year at which Earth Meteorite was hit"][i] != None:
        if df1["Year at which Earth Meteorite was hit"][i].year < 2000:
            var.append(df1["Name of Earth Meteorite"][i])
print(f"There are total {len(var)} such Earth Meteorites and are listed below:\n")
print(var)
print("\n")


# Get all the earth meteorites co-ordinates who fell before the year 1970
print("Insight: Get all the earth meteorites co-ordinates who fell before the year 1970\n")
var = []
for i in range(len(df1["Name of Earth Meteorite"])):
    if df1["Year at which Earth Meteorite was hit"][i] != None:
        if df1["Year at which Earth Meteorite was hit"][i].year < 1970:
            var.append(df1["point coordinates"][i])
print(f"There are total {len(var)} such Earth Meteorites and their coordinates are listed below:\n")
print(var)
print("\n")


# Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more than 10000kg
print("Insight: Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more than 10000kg\n")
var = []
for i in range(len(df1["Name of Earth Meteorite"])):
    if df1["Mass of Earth Meteorite"][i] != None:
        if df1["Mass of Earth Meteorite"][i] > 10000:
            var.append(df1["Name of Earth Meteorite"][i])
print(f"There are total {len(var)} such Earth Meteorites and are listed below:\n")
print(var)
print("\n")