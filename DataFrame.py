#Creating a dataframe
import pandas as pd
data={
    "Name": ["Hari", "Ram", "Alex"],
    "Marks": [85, 90, 95],
    "Grade": ["A", "A+", "A+"]
} 
df=pd.DataFrame(data)
print(df)

#Dataframe attributes
print(df.columns)
print(df.shape)
print(df.dtypes)

#dataframe attributes
import pandas as pd
df = pd.DataFrame({
    "Name": ["Hari", "Ram"],
    "Age": [21, 22]
})

print("Shape:", df.shape)
print("Columns:", df.columns)
print("Dimensions:", df.ndim)
print("Size:", df.size)
print("Types:\n", df.dtypes)



