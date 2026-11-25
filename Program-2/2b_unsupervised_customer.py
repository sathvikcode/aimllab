import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("customer_segmentation.csv")
X = data[["Age", "Income", "SpendingScore"]]

model = KMeans(n_clusters=3, random_state=42)
data["Cluster"] = model.fit_predict(X)
print(data)

age = int(input("Enter Age: "))
income = int(input("Enter Income: "))
score = int(input("Enter Spending Score: "))

customer = pd.DataFrame([[age, income, score]], columns=X.columns)
cluster = model.predict(customer)
print("Customer belongs to Cluster", cluster[0])
