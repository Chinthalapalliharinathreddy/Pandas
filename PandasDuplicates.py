import numpy as np
import pandas as pd

df=pd.DataFrame({
    "ID":[1,2,2,3],
    "Names":["Hari","Ram","Ram","Alex"]
})
#print(df)
print(df.duplicated())
print(df.duplicated().sum())
df.drop_duplicates()

print(df)