# importing required libraries
import pandas as pd
import warnings
import pickle
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

# ignoring warnings
warnings.filterwarnings('ignore')

# reading data from csv file
df = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

# encodeing 0 and 1 for columns with binary classification
binary_col = ["family_history_with_overweight", "FAVC", "SMOKE", "SCC"]
for i in binary_col:
    for j in range(len(df)):
        if df[i].iloc[j] == "yes":
            df[i].iloc[j] = 1
        else:
            df[i].iloc[j] = 0
for i in range(len(df)):
    if df["Gender"].iloc[i] == "Female":
        df["Gender"].iloc[i] = 1
    else:
        df["Gender"].iloc[i] = 0

# converting excoded column's datatypes to float
for col in binary_col:
    df[col] = df[col].astype("float")
df["Gender"] = df["Gender"].astype("float")

# making separate dataframes for numerical and categorical variables
df_numeric = pd.DataFrame()
df_cat = pd.DataFrame()
for column in df.columns:
    if df[column].dtype == "float64":
        df_numeric[column] = df[column]
    else:
        df_cat[column] = df[column]
# removing output column
df_cat = df_cat.drop("NObeyesdad", axis = 1)

# encoding categorical columns using one hot encoding
encoder = OneHotEncoder()
enc = encoder.fit_transform(df_cat).toarray()
col_name = list(encoder.get_feature_names_out(df_cat.columns))

encoded_results = pd.DataFrame(enc, columns = col_name)

# joining the numerical and encoded columns to get all the input columns
X = df_numeric.join(encoded_results)

# encoding output column
y = []
for i in range(len(df)):
    if df["NObeyesdad"].iloc[i] == "Insufficient_Weight":
        y.append(1)
    elif df["NObeyesdad"].iloc[i] == "Normal_Weight":
        y.append(2)
    elif df["NObeyesdad"].iloc[i] in ["Overweight_Level_I","Overweight_Level_II"]:
        y.append(3)
    elif df["NObeyesdad"].iloc[i] in ["Obesity_Type_I", "Obesity_Type_II"]:
        y.append(4)
    elif df["NObeyesdad"].iloc[i] == "Obesity_Type_III":
        y.append(5)
y = pd.Series(y, dtype = int)

# spliting data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# considering 4 models for classification
models = [RandomForestClassifier(), KNeighborsClassifier(n_neighbors=5), DecisionTreeClassifier(random_state=10), GradientBoostingClassifier(n_estimators=20, learning_rate=1.0, max_depth=1, random_state=0)]

# selecting best model based on accuracy score
for model in models:
    score = []
    model.fit(X_train, y_train)
    score.append(model.score(X_test, y_test))

best_model = models[score.index(max(score))]

# creating pickle file for best model
best_model.fit(X_train, y_train)
pickle.dump(best_model, open('modelQ2.pkl', 'wb'))

# loading pickle model to predict output
pickled_model = pickle.load(open('modelQ2.pkl', 'rb'))

while True:
    # using try and except block to catch invalid inputs
    try:
        # Taking input
        new_input = []
        print("\nPlease enter following inputs\n")
        inp = input("Gender (Male/ Female):\n")
        if inp.lower() == "female":
            new_input.append(1)
        elif inp.lower() == "male":
            new_input.append(0)
        inp = int(input("Age:\n"))
        new_input.append(inp)
        inp = int(input("Height:\n"))
        new_input.append(inp)
        inp = int(input("Weight:\n"))
        new_input.append(inp)
        inp = input("Family history with overweight (yes/ no):\n")
        if inp.lower() == "yes":
            new_input.append(1)
        else:
            new_input.append(0)
        inp = input("Frequent consumption of high caloric food (yes/ no):\n")
        if inp.lower() == "yes":
            new_input.append(1)
        else:
            new_input.append(0)
        inp = int(input("Frequency of consumption of vegetables:\n"))
        new_input.append(inp)
        inp = int(input("Number of main meals:\n"))
        new_input.append(inp)
        inp = input("Smoke (yes/ no):\n")
        if inp.lower() == "yes":
            new_input.append(1)
        else:
            new_input.append(0)
        inp = int(input("Consumption of water daily:\n"))
        new_input.append(inp)
        inp = input("Calories consumption monitoring (yes/ no):\n")
        if inp.lower() == "yes":
            new_input.append(1)
        else:
            new_input.append(0)
        inp = int(input("Physical activity frequency:\n"))
        new_input.append(inp)
        inp = int(input("Time using technology devices:\n"))
        new_input.append(inp)
        inp = input("Consumption of food between meals (Always/ Frequently/ Sometimes/ no):\n")
        a = ["always", "frequently", "sometimes", "no"]
        b = [0,0,0,0]
        if inp.lower() in a:
            b[a.index(inp.lower())] = 1
            new_input = new_input + b
        inp = input("Consumption of alcohol (Always/ Frequently/ Sometimes/ no):\n")
        a = ["always", "frequently", "sometimes", "no"]
        b = [0,0,0,0]
        if inp.lower() in a:
            b[a.index(inp.lower())] = 1
            new_input = new_input + b
        inp = input("Consumption of alcohol (Automobile/ Bike/ Motorbike/ Public_Transportation/ Walking):\n")
        a = ["automobile", "bike", "motorbike", "public_transportation", "walking"]
        b = [0,0,0,0,0]
        if inp.lower() in a:
            b[a.index(inp.lower())] = 1
            new_input = new_input + b
        
        # Calculating output based on the pickle model after scaling
        y = pickled_model.predict(np.array(new_input).reshape(1,26))
        
        op = ["Underweight", "Normal", "Overweight", "Obese", "Extremely Obese"]
        
        print(f"\nBased on input data the person is {op[int(y[0])-1]}\n")
        
    except ValueError:
        print("Invalid Input")
