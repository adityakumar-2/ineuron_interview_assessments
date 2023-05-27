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

# Saving the file in CSV fomat without index
df1.to_csv("meteorite_data.csv", index = False)