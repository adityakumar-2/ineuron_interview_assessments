import csv
import requests
import pandas as pd

CSV_URL = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
#columns = my_list[0]
df = pd.DataFrame(my_list[1:], columns = my_list[0])

# converting required columns into integers

df["Model Year"] = pd.Series(df["Model Year"], dtype = int)
df["Electric Range"] = pd.Series(df["Electric Range"], dtype = int)

#  Get all the cars and their types that do not qualify for clean alternative fuel vehicle
print("Insight: Get all the cars and their types that do not qualify for clean alternative fuel vehicle\n")
new_df = pd.DataFrame()
new_df = df[["Model Year", "Make", "Model", "Electric Vehicle Type"]][df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"] == 'Not eligible due to low battery range']
var = []
for i in range(len(new_df)):
    var.append(str(new_df["Model Year"].iloc[i]) + " " + new_df["Make"].iloc[i] + " "+ new_df["Model"].iloc[i] +" "+ new_df["Electric Vehicle Type"].iloc[i])
print(f"There are total {len(var)} such vehilces and are listed below:\n")
print(var)
print("\n")

# Get all TESLA cars with the model year, and model type made in Bothell City
print("Insight: Get all TESLA cars with the model year, and model type made in Bothell City\n")
new_df = pd.DataFrame()
new_df = df[["Model Year", "Model"]][(df["Make"] == 'TESLA') & (df["City"] == 'Bothell')]
var = []
for i in range(len(new_df)):
    var.append(str(new_df["Model Year"].iloc[i]) + " " + new_df["Model"].iloc[i])
print(f"There are total {len(var)} such vehilces and are listed below:\n")
print(var)
print("\n")

# Get all the cars that have an electric range of more than 100, and were made after 2015
print("Insight: Get all the cars that have an electric range of more than 100, and were made after 2015\n")
new_df = pd.DataFrame()
new_df = df[["Model Year","Make", "Model"]][(df["Electric Range"] > 100) & (df["Model Year"] > 2015)]
var = []
for i in range(len(new_df)):
    var.append(str(new_df["Model Year"].iloc[i]) + " " + new_df["Make"].iloc[i] + " "+ new_df["Model"].iloc[i])
print(f"There are total {len(var)} such vehilces and are listed below:\n")
print(var)
print("\n")

#  Draw plots to show the distribution between city and electric vehicle type
print("Insight: Draw plots to show the distribution between city and electric vehicle type\n")
CrosstabResult=pd.crosstab(index=df['City'],columns=df['Electric Vehicle Type'], dropna=True)
CrosstabResult.plot(kind="barh", figsize = (5,110))