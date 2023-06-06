# importing required libraries
import pandas as pd
import nltk
import re
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

# reading data
d = pd.read_json("News_Category_Dataset_v3.json", lines=True)

# retaining only 50000 data points
data = d.iloc[:50000]

# creating a combination of headline and short description
com = []
for i in range(len(data)):
    com.append(data["headline"].iloc[i]+" " +data["short_description"].iloc[i])

# cleaning data
ps=PorterStemmer()

corpus=[]
for i in range(0,len(com)):
    review=re.sub('[^a-zA-Z]'," ",com[i])
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if word not in stopwords.words("english")]
    review=" ".join(review)
    corpus.append(review)

# vactorizing data for input into ML algorithms
vectorizer = CountVectorizer(max_features=2500)
X = vectorizer.fit_transform(corpus).toarray()

# assigning categories to utput data
y = []
cat = list(data["category"].unique())
for i in data["category"]:
    y.append(cat.index(i))

# test train split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# testing 4 models and selecting the best one
models = [RandomForestClassifier(n_estimators=2, max_depth=1), KNeighborsClassifier(n_neighbors=41), MultinomialNB(), GradientBoostingClassifier(n_estimators=2, learning_rate=1.0, max_depth=1, random_state=0)]
for model in models:
    score = []
    model.fit(X_train, y_train)
    score.append(model.score(X_test, y_test))

best_model = models[score.index(max(score))]

# creating pickle file for best model
best_model.fit(X_train, y_train)
pickle.dump(best_model, open('modelQ3.pkl', 'wb'))

# loading pickle model to predict output
pickled_model = pickle.load(open('modelQ3.pkl', 'rb'))

while True:
    try:
        # taking input
        inp = []
        inp.append(input("Enter the headline and short description:\n"))

        # processing input
        corpus=[]
        for i in range(0,len(inp)):
            review=re.sub('[^a-zA-Z]'," ",inp[i])
            review=review.lower()
            review=review.split()
            review=[ps.stem(word) for word in review if word not in stopwords.words("english")]
            review=" ".join(review)
            corpus.append(review)

        inp_t = vectorizer.transform(corpus).toarray()

        # Calculating output based on the pickle model
        y = pickled_model.predict(inp_t)

        # displaying output
        print(f"Category is {cat[y[0]]}")
    except ValueError:
        print("Invalid Input")