# importing required modules
import pandas as pd
import numpy as np
import warnings
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ignoring warnings
warnings.filterwarnings('ignore')

# reading data from CSV
data = pd.read_csv("online_shoppers_intention.csv")

# converting months into numbers
months = {'Jan': 1, 'Feb':2, 'Mar':3, 'April':4, 'May':5, 'June':6, 'Jul':7, 'Aug':8,'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

for i in range(len(data)):
    key = months[data["Month"].iloc[i]]
    data["Month"].iloc[i] = key

# cganging data type of Months column to int
data["Month"] = data["Month"].astype(int)

# encoding Visitors type column
encoder = OneHotEncoder()
enc = encoder.fit_transform(np.array(data["VisitorType"]).reshape(-1,1)).toarray()
col_name = list(encoder.get_feature_names_out(data[["VisitorType"]].columns))

encoded_results = pd.DataFrame(enc, columns = col_name)

encoded_results = encoded_results.drop("VisitorType_Other", axis =1)

# craeting new dataframe for input variables
X = data.drop(["Weekend", "Revenue", "VisitorType"], axis = 1).join(encoded_results)

# creating dataframe for output variables
y = pd.DataFrame(columns = ["Weekend", "Revenue"])
y["Weekend"] = data["Weekend"].astype(int)
y["Revenue"] = data["Revenue"].astype(int)

# creating train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Training random forest model and creating picke file
model1 = RandomForestClassifier()
model1.fit(X_train, y_train["Weekend"])
pickle.dump(model1, open('modelQ3a.pkl', 'wb'))

model2 = RandomForestClassifier()
model2.fit(X_train, y_train["Revenue"])
pickle.dump(model2, open('modelQ3b.pkl', 'wb'))


# loading pickle model to predict output
pickled_model1 = pickle.load(open('modelQ3a.pkl', 'rb'))
pickled_model2 = pickle.load(open('modelQ3b.pkl', 'rb'))

while True:
    # using try and except block to catch invalid inputs
    try:
        # Taking input
        new_input = []
        print("\nPlease enter following inputs\n")
        inp = int(input("No. of Administrative pages:\n"))
        new_input.append(inp)
        inp = int(input("Time spend on Administrative pages:\n"))
        new_input.append(inp)
        inp = int(input("No. of Informational pages:\n"))
        new_input.append(inp)
        inp = int(input("Time spent on Informational pages:\n"))
        new_input.append(inp)
        inp = int(input("NoProductRelated:\n"))
        new_input.append(inp)
        inp = int(input("ProductRelated_Duration:\n"))
        new_input.append(inp)
        inp = int(input("BounceRates:\n"))
        new_input.append(inp)
        inp = int(input("ExitRates:\n"))
        new_input.append(inp)
        inp = int(input("PageValues:\n"))
        new_input.append(inp)
        inp = int(input("SpecialDay:\n"))
        new_input.append(inp)
        inp = int(input("Month Number (between 1 to 12):\n"))
        new_input.append(inp)
        inp = int(input("OperatingSystems:\n"))
        new_input.append(inp)
        inp = int(input("Browser:\n"))
        new_input.append(inp)
        inp = input("Region:\n")
        new_input.append(inp)
        inp = input("TrafficType:\n")
        new_input.append(inp)
        inp = input("Visitor Type (Returning/ New/ Other):\n")
        a = ["returning", "new"]
        b = [0,0]
        if inp.lower() in a:
            b[a.index(inp.lower())] = 1
            new_input = new_input + b
        else:
            new_input = new_input + b
        
        # Calculating output based on the pickle model after scaling
        y1 = pickled_model1.predict(np.array(new_input).reshape(1,17))
        y2 = pickled_model2.predict(np.array(new_input).reshape(1,17))

        if y1[0] == 1 and y2[0] ==1:
            print("\nThe personn will generate revenue on weekend\n")
        elif y1[0] == 1 and y2[0] ==0:
            print("\nThe personn will generate revenue but not on weekend\n")
        elif y1[0] == 0:
            print("\nThe person will not generate revenue\n")
        
    except ValueError:
        print("Invalid Input")

