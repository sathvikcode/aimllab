import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv("diabetes.csv")
X = data[["Glucose", "BloodPressure", "BMI", "Age"]]
y = data["Diabetes"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential([
    Dense(8, activation="relu", input_shape=(4,)),
    Dense(4, activation="relu"),
    Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=100, batch_size=4, verbose=0)

prediction = model.predict(X_test, verbose=0) > 0.5
print("Model Accuracy: {:.2f}%".format(accuracy_score(y_test, prediction) * 100))

glucose = float(input("Enter Glucose Level: "))
bp = float(input("Enter Blood Pressure: "))
bmi = float(input("Enter BMI: "))
age = float(input("Enter Age: "))

patient = pd.DataFrame({
    "Glucose": [glucose], "BloodPressure": [bp], "BMI": [bmi], "Age": [age]
})
result = model.predict(scaler.transform(patient), verbose=0)

print("Patient is Diabetic" if result[0][0] > 0.5 else "Patient is Non-Diabetic")
