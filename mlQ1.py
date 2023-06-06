import re
import pandas as pd
import numpy as np
import warnings
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

  
# Settings the warnings to be ignored
warnings.filterwarnings('ignore')

# Loading data from CSV file to train model
df = pd.read_csv("instagram_reach.csv")
df = df.drop("Unnamed: 0", axis = 1)

# converting "time since posted" to number of hours since posted
for i in range(len(df)):
    df["Time since posted"].iloc[i] = int(df["Time since posted"].iloc[i].split()[0])
    
# counting number of hashtags
var = []
for i in range(len(df)):
    var.append(len(re.split("\xa0#|\xa0.#|#",df["Hashtags"].iloc[i])))
df["hash_len"] = pd.Series(var, dtype = int)

# determining length of captions
var = []
for i in range(len(df)):
    var.append(len(str(df["Caption"].iloc[i])))
df["caption_len"] = pd.Series(var, dtype = int)

# droping columns which are not required
df1 = df.drop(["S.No", "USERNAME", "Caption", "Hashtags"], axis = 1)

# defining independent and dependent variables
X = df1.drop("Likes", axis =1)
y = df1["Likes"]

# Splitting initial data into test and train data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Scalaing the independent variables
scaler=StandardScaler()
scaler.fit(X_train)
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# model selection based on r2 score and generate pickle file
def model_selector(X_train, X_test, y_train, y_test):
    models = [LinearRegression(), Ridge(alpha = 10), Lasso(alpha = 10), ElasticNet(alpha = 10)]
    score = []
    for model in models:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score.append(r2_score(y_test,y_pred))
    best_model =  models[score.index(max(score))]
    best_model.fit(X_train, y_train)
    pickle.dump(best_model, open('modelQ1.pkl', 'wb'))

# calling function to select best model and generate pickle file
model_selector(X_train, X_test, y_train, y_test)

# loading pickle file to predict output
pickled_model = pickle.load(open('modelQ1.pkl', 'rb'))


# using while loop to continuously take inputs and return outputs
while True:
    # using try and except block to catch invalid inputs
    try:
        # Taking input for predicting number of likes
        new_input = []
        print("\nPlease enter following inputs to predict the number of likes on the instagram post\n")
        inp = int(input("Number of Followers:\n"))
        new_input.append(inp)
        inp = int(input("Number of Hours since posted:\n"))
        new_input.append(inp)
        inp = int(input("Number of Hashtags:\n"))
        new_input.append(inp)
        inp = int(input("Length of Caption:\n"))
        new_input.append(inp)
        
        # Calculating output based on the pickle model after scaling
        y = pickled_model.predict(scaler.transform(np.array(new_input).reshape(1,4)))
        print(f"Estimated number of Likes is {max(0,int(y))}\n")
    except ValueError:
        print("Only integer values allowed")
    

