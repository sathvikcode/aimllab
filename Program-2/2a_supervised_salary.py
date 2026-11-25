import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("emp_salary.csv")
X = data[["Age", "Experience", "Education"]]
y = data["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("Actual Values:", y_test.values)
print("Predicted Values:", prediction)
print("Accuracy: {:.2f}%".format(accuracy_score(y_test, prediction) * 100))

age = int(input("Enter Age: "))
exp = int(input("Enter Experience: "))
edu = int(input("Enter Education Years: "))
employee = pd.DataFrame([[age, exp, edu]], columns=X.columns)
result = model.predict(employee)

if result[0] == "High":
    print("High Salary Employee")
else:
    print("Low Salary Employee")
