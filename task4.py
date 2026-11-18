#Create a Pandas Series
import pandas as pd
marks = pd.Series([85, 90, 75, 80, 95])
print("Pandas Series:")
print(marks)

#Create a Pandas DataFrame

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Age': [20, 21, 19, 20],
    'Marks': [85, 90, 75, 80]
}
df = pd.DataFrame(data)
print(df)

#Ddisplay Column Names

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 75]
}
df = pd.DataFrame(data)
print("\nColumn Names:")
print(df.columns)

#Display Index

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Marks': [85, 90, 75]
}
df = pd.DataFrame(data)
print("Index:")
print(df.index)

#Add a New Column

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Marks': [85, 90, 75]
}
df = pd.DataFrame(data)
df['City'] = ['Pune', 'Mumbai', 'Nagpur']
print(df)
