import pandas as pd

# Step 1: Create employee dataset
data = {
    "EmployeeID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Hari", "Ram", "Alex", "John", "Sam", "David", "Ravi"],
    "Age": [22, 25, 28, 35, 30, 40, 27],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales", "IT"],
    "Salary": [50000, 45000, 60000, 70000, 55000, 80000, 65000]
}

df = pd.DataFrame(data)

# Step 2: Save dataset as CSV
df.to_csv("employees.csv", index=False)

# Step 3: Read CSV file
df = pd.read_csv("employees.csv")

print("----- Employee Dataset -----")
print(df)

# Step 4: Basic information
print("\n----- Basic Information -----")
print("Total Employees:", len(df))
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# Step 5: Salary analysis
print("\n----- Salary Analysis -----")
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print("Total Salary:", df["Salary"].sum())

# Step 6: Highest paid employee
print("\n----- Highest Paid Employee -----")
highest_paid = df[df["Salary"] == df["Salary"].max()]
print(highest_paid)

# Step 7: Lowest paid employee
print("\n----- Lowest Paid Employee -----")
lowest_paid = df[df["Salary"] == df["Salary"].min()]
print(lowest_paid)

# Step 8: Filtering
print("\n----- IT Employees -----")
print(df[df["Department"] == "IT"])

print("\n----- Employees Older Than 30 -----")
print(df[df["Age"] > 30])

print("\n----- Employees Salary Greater Than 60000 -----")
print(df[df["Salary"] > 60000])

# Step 9: Multiple condition filtering
print("\n----- IT Employees With Salary Greater Than 55000 -----")
print(df[(df["Department"] == "IT") & (df["Salary"] > 55000)])

# Step 10: GroupBy analysis
print("\n----- Average Salary By Department -----")
print(df.groupby("Department")["Salary"].mean())

print("\n----- Total Salary By Department -----")
print(df.groupby("Department")["Salary"].sum())

print("\n----- Employee Count By Department -----")
print(df.groupby("Department").size())

print("\n----- Maximum Salary By Department -----")
print(df.groupby("Department")["Salary"].max())

print("\n----- Minimum Salary By Department -----")
print(df.groupby("Department")["Salary"].min())

# Step 11: Sorting
print("\n----- Employees Sorted By Salary High To Low -----")
print(df.sort_values("Salary", ascending=False))

print("\n----- Employees Sorted By Age Low To High -----")
print(df.sort_values("Age"))

# Step 12: String operations
df["Name_Upper"] = df["Name"].str.upper()
df["Department_Lower"] = df["Department"].str.lower()

print("\n----- After String Operations -----")
print(df)

# Step 13: Add bonus column
df["Bonus"] = df["Salary"] * 0.10

# Step 14: Add total compensation column
df["Total_Compensation"] = df["Salary"] + df["Bonus"]

# Step 15: Add tax column
df["Tax"] = df["Salary"] * 0.05

# Step 16: Final salary after tax
df["Final_Salary"] = df["Total_Compensation"] - df["Tax"]

print("\n----- Final Employee Data -----")
print(df)

# Step 17: Employees earning more than average salary
average_salary = df["Salary"].mean()

print("\n----- Employees Earning More Than Average Salary -----")
print(df[df["Salary"] > average_salary])

# Step 18: Oldest employee
print("\n----- Oldest Employee -----")
print(df[df["Age"] == df["Age"].max()])

# Step 19: Youngest employee
print("\n----- Youngest Employee -----")
print(df[df["Age"] == df["Age"].min()])

# Step 20: Department with highest average salary
dept_avg_salary = df.groupby("Department")["Salary"].mean()
highest_avg_dept = dept_avg_salary.idxmax()

print("\n----- Department With Highest Average Salary -----")
print(highest_avg_dept)

# Step 21: Save final analysis
df.to_csv("employee_analysis.csv", index=False)

print("\nProject completed successfully!")
print("Final file saved as employee_analysis.csv")