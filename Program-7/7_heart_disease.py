import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

data = pd.read_csv("heart_disease.csv")
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = GaussianNB()
model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("Accuracy: {:.2f}%".format(accuracy_score(y_test, prediction) * 100))
print("Precision: {:.2f}%".format(precision_score(y_test, prediction, zero_division=0) * 100))
print("Recall: {:.2f}%".format(recall_score(y_test, prediction, zero_division=0) * 100))
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))

age = int(input("Enter Age: "))
bp = int(input("Enter Blood Pressure: "))
chol = int(input("Enter Cholesterol: "))
hr = int(input("Enter Maximum Heart Rate: "))
cp = int(input("Chest Pain (0=No, 1=Yes): "))

patient = pd.DataFrame([[age, bp, chol, hr, cp]], columns=X.columns)
result = model.predict(patient)
print("Heart Disease Detected" if result[0] == 1 else "No Heart Disease")
