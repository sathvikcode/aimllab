import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("iris.csv", sep="\t")
X = data.iloc[:, 1:-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
prediction = model.predict(X_test)

correct = wrong = 0
for actual, predicted in zip(y_test, prediction):
    print("Actual:", actual, "| Predicted:", predicted)
    if actual == predicted:
        print("Correct Prediction")
        correct += 1
    else:
        print("Wrong Prediction")
        wrong += 1

print("Correct Predictions:", correct)
print("Wrong Predictions:", wrong)
print("Accuracy: {:.2f}%".format(accuracy_score(y_test, prediction) * 100))

sl = float(input("Enter Sepal Length: "))
sw = float(input("Enter Sepal Width: "))
pl = float(input("Enter Petal Length: "))
pw = float(input("Enter Petal Width: "))

flower = pd.DataFrame([[sl, sw, pl, pw]], columns=X.columns)
print("Predicted Flower Species:", model.predict(flower)[0])
