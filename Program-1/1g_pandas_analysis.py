import pandas as pd

data = {
    "Name": ["Ravi", "Arpitha", "Arun", "Pooja", "Sneha"],
    "Marks": [89, 74, 95, 68, 80],
    "Department": ["CSE", "ECE", "CSE", "EEE", "ECE"]
}

df = pd.DataFrame(data)
print(df)
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])
print("\nDepartment Wise Average:")
print(df.groupby("Department")["Marks"].mean())
