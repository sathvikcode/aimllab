import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = pd.read_csv("emailspam.csv")
X = data["Message"]
y = data["Category"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("Actual Values:", y_test.values)
print("Predicted Values:", prediction)
print("Accuracy: {:.2f}%".format(accuracy_score(y_test, prediction) * 100))

email = input("Enter Email Message: ")
result = model.predict(vectorizer.transform([email]))
print("Spam Email" if result[0] == "Spam" else "Not Spam Email")
