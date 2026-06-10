import pandas as pd

df = pd.DataFrame({
    "Name": ["Hari", "Ram", "Alex", "John", "Sam"],
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Salary": [50000, 40000, 60000, 45000, 70000]
})

print(df)

df.groupby("Department")
print(df.groupby("Department").count())
print(df.groupby("Department")["Salary"].sum())
print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())
print(df.groupby("Department")["Salary"].std())
print(df.groupby("Department")["Salary"].describe())
groups = df.groupby("Department")

print(groups.get_group("IT"))

print(df.groupby(["Department","Department"]))