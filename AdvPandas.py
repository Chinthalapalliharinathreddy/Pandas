import numpy as np
import pandas as pd

df=pd.DataFrame({
    "Name":["Hari","Ram","Alex"],
    "Age":[22,np.nan,28],
    "Salary":[50000,45000,np.nan]
})

print(df)
print(df.isnull())
print(df.dropna())
print(df.dropna(axis=1))
print(df.fillna(0))
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df["Age"])
print(df)
df["Salary"]=df["Salary"].fillna(df["Salary"].mode()[0])
print(df)

