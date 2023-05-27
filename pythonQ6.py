# importing required libraries
import urllib.request
import json 
import pandas as pd

# reading data from provided URL
url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

# converting data froom dict to DataFrame
df = pd.DataFrame(data["pokemon"])

#initializing a new dataframe to store the data in correct data types
df1 = pd.DataFrame()

# setting correct datatypes
df1["Identification Number"] = pd.Series(df["id"], dtype = int)
df1["Number of the Pokémon in the official Pokédex"] = pd.Series(df["num"], dtype = int)
df1["Pokémon name"] = pd.Series(df["name"], dtype = str)
df1["URL to an image of this Pokémon"] = pd.Series(df["img"], dtype = str)
df1["Pokémon type"] = pd.Series(df["type"], dtype = object)

# removing the units from height, weight and eggs columns
height = []
for i in range((len(data["pokemon"]))):
    try:
        height.append(float(data["pokemon"][i]["height"].split()[0]))
    except:
        height.append(0)
df1["Pokémon height"] = pd.Series(height, dtype = float)

weight = []
for i in range((len(data["pokemon"]))):
    try:
        weight.append(float(data["pokemon"][i]["weight"].split()[0]))
    except:
        weight.append(0)
df1["Pokémon weight"] = pd.Series(weight, dtype = float)

df1["type of candy used to evolve Pokémon or given when transferred"] = pd.Series(df["candy"], dtype = str)
df1["the amount of candies required to evolve"] = pd.Series(df["candy_count"], dtype = int)

eggs = []
for i in range((len(data["pokemon"]))):
    try:
        eggs.append(float(data["pokemon"][i]["egg"].split()[0]))
    except:
        eggs.append(0)
df1["Number of kilometers to travel to hatch the egg"] = pd.Series(eggs, dtype = int)

df1["Percentage of spawn chance (NEW)"] = pd.Series(df["spawn_chance"], dtype = float)
df1["Number of this pokemon on 10.000 spawns (NEW)"] = pd.Series(df["avg_spawns"], dtype = int)
df1["Spawns most active at the time on this field"] = pd.Series(df["spawn_time"], dtype = str)
df1["Multiplier of Combat Power"] = pd.Series(df["multipliers"], dtype = object)
df1["Types of Pokémon this Pokémon is weak to"] = pd.Series(df["weaknesses"], dtype = object)
df1["Number and Name of successive evolutions of Pokémon"] = pd.Series(df["next_evolution"], dtype = object)
df1["Number and Name of previous evolutions of Pokémon"] = pd.Series(df["prev_evolution"], dtype = object)



# Get all Pokemons whose spawn rate is less than 5%
print("Insight: Get all Pokemons whose spawn rate is less than 5%\n")
var = []
for i in range(len(df1["Pokémon name"])):
    if df1["Percentage of spawn chance (NEW)"].iloc[i]<5:
        var.append(df1["Pokémon name"].iloc[i])
print(f"There are total {len(var)} such Pokemons and are listed below:\n")
print(var)
print("\n")


# Get all Pokemons that have less than 4 weaknesses
print("Ingight: Get all Pokemons that have less than 4 weaknesses\n")
var = []
for i in range(len(df1["Pokémon name"])):
    if len(df1["Types of Pokémon this Pokémon is weak to"].iloc[i])<4:
        var.append(df1["Pokémon name"].iloc[i])
print(f"There are total {len(var)} such Pokemons and are listed below:\n")
print(var)
print("\n")


# Get all Pokemons that have no multipliers at all
print("Insight: Get all Pokemons that have no multipliers at all\n")
var = []
for i in range(len(df1["Pokémon name"])):
    if df1["Multiplier of Combat Power"].iloc[i] == None:
        var.append(df1["Pokémon name"].iloc[i])
print(f"There are total {len(var)} such Pokemons and are listed below:\n")
print(var)
print("\n")


# Get all Pokemons that do not have more than 2 evolutions
print("Ingight: Get all Pokemons that do not have more than 2 evolutions\n")
var = []
for i in range(len(df1["Pokémon name"])):
    if type(df1["Number and Name of successive evolutions of Pokémon"].iloc[i]) == list:
        if len(df1["Number and Name of successive evolutions of Pokémon"].iloc[i]) <= 2:
            var.append(df1["Pokémon name"].iloc[i])
print(f"There are total {len(var)} such Pokemons and are listed below:\n")
print(var)
print("\n")


# Get all Pokemons whose spawn time is less than 300 seconds
print("Insight: Get all Pokemons whose spawn time is less than 300 seconds\n")
var = []
for i in range(len(df1["Pokémon name"])):
    if df1["Spawns most active at the time on this field"].iloc[i] != "N/A":
        minute = int(df1["Spawns most active at the time on this field"].iloc[i].split(":")[0])
        sec = int(df1["Spawns most active at the time on this field"].iloc[i].split(":")[1])
        if minute*60+sec < 300:
            var.append(df1["Pokémon name"].iloc[i])
print(f"There are total {len(var)} such Pokemons and are listed below:\n")
print(var)
print("\n")


# Get all Pokemon who have more than two types of capabilities
print("Insight: Get all Pokemon who have more than two types of capabilities\n")
var = []
for i in range(len(df1["Pokémon name"])):
    if len(df1["Pokémon type"].iloc[i]) > 2:
        var.append(df1["Pokémon name"].iloc[i])
print(f"There are total {len(var)} such Pokemons\n")
print("\n")