import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("employee_salary.csv")
X = data[["Age", "Experience", "Salary"]]

model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)
data["Cluster"] = model.labels_

print("Employee Clusters:\n", data)
print("Cluster Centers:\n", pd.DataFrame(model.cluster_centers_, columns=X.columns))

age = int(input("Enter Age: "))
exp = int(input("Enter Experience: "))
salary = int(input("Enter Salary: "))

employee = pd.DataFrame([[age, exp, salary]], columns=X.columns)
cluster = model.predict(employee)[0]
print("Employee belongs to Cluster:", cluster)

if cluster == 0:
    print("Category: Junior Employee")
elif cluster == 1:
    print("Category: Mid-Level Employee")
else:
    print("Category: Senior Employee")
