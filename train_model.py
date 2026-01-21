import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

data = pd.read_csv("dataset.csv")

X = data["message"]
y = data["label"]

vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vector, y)

pickle.dump(model, open("scam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully!")
