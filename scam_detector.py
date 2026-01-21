import pickle

model = pickle.load(open("scam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

message = input("Enter message: ")

data = vectorizer.transform([message])
prediction = model.predict(data)

if prediction[0] == "scam":
    print("⚠️ Scam Detected!")
else:
    print("✅ Message is Safe")
