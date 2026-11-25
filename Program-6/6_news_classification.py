import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = pd.read_csv("news_dataset.csv")
X = data["Document"]
y = data["Category"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("Accuracy: {:.2f}%".format(accuracy_score(y_test, prediction) * 100))
print("Precision: {:.2f}%".format(precision_score(y_test, prediction, average="weighted", zero_division=0) * 100))
print("Recall: {:.2f}%".format(recall_score(y_test, prediction, average="weighted", zero_division=0) * 100))

news = input("Enter News Article: ")
predicted = model.predict(vectorizer.transform([news]))[0]
print("Predicted Category:", predicted)

actual = input("Enter Actual Category: ")
print("Correct" if predicted.lower() == actual.lower() else "Incorrect")
