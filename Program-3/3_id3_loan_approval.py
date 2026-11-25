import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("loan_approval.csv")
X = data[["Age", "Income", "CreditScore", "Experience"]]
y = data["LoanApproved"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("Actual Values:", y_test.values)
print("Predicted Values:", prediction)
print("Accuracy:", accuracy_score(y_test, prediction) * 100)

age = int(input("Enter Age: "))
income = int(input("Enter Monthly Income: "))
credit = int(input("Enter Credit Score: "))
experience = int(input("Enter Years of Experience: "))

customer = pd.DataFrame(
    [[age, income, credit, experience]], columns=X.columns
)
result = model.predict(customer)

print("Loan Approved" if result[0] == "Yes" else "Loan Rejected")
