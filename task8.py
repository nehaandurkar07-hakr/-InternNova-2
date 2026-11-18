#Merge Two DataFrames

import pandas as pd
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Rahul', 'Priya', 'Amit']
})
df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Marks': [85, 90, 75]
})
result = pd.merge(df1, df2, on='ID')
print(result)
print("\n")


#Concatenate Two DataFrames

import pandas as pd
df1 = pd.DataFrame({
    'Name': ['Rahul', 'Priya'],
    'Marks': [85, 90]
})
df2 = pd.DataFrame({
    'Name': ['Amit', 'Neha'],
    'Marks': [75, 80]
})
result = pd.concat([df1, df2], ignore_index=True)
print(result)
print("\n")


#GroupBy with Sum

import pandas as pd
data = {
    'Department': ['IT', 'HR', 'IT', 'HR'],
    'Salary': [30000, 25000, 40000, 35000]
}
df = pd.DataFrame(data)
result = df.groupby('Department')['Salary'].sum()
print(result)
print("\n")


#GroupBy with Mean

import pandas as pd
data = {
    'Department': ['IT', 'HR', 'IT', 'HR'],
    'Salary': [30000, 25000, 40000, 35000]
}
df = pd.DataFrame(data)
result = df.groupby('Department')['Salary'].mean()
print(result)
print("\n")


#GroupBy with Count, Minimum and Maximum

import pandas as pd
data = {
    'Department': ['IT', 'HR', 'IT', 'HR'],
    'Salary': [30000, 25000, 40000, 35000]
}
df = pd.DataFrame(data)
print("Count:")
print(df.groupby('Department')['Salary'].count())
print("Minimum:")
print(df.groupby('Department')['Salary'].min())
print("Maximum:")
print(df.groupby('Department')['Salary'].max())
print("\n")


#Create a Pivot Table

import pandas as pd
data = {
    'Department': ['IT', 'HR', 'IT', 'HR'],
    'Salary': [30000, 25000, 40000, 35000]
}
df = pd.DataFrame(data)
result = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    aggfunc='mean'
)
print(result)
