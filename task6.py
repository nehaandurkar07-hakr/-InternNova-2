#Select a Single Column

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Age': [20, 21, 19, 20],
    'Marks': [85, 90, 75, 80]
}
df = pd.DataFrame(data)
print(df['Name'])

#Select Multiple Columns

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 75]
}
df = pd.DataFrame(data)
print(df[['Name', 'Marks']])

#Select Specific Rows

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Marks': [85, 90, 75, 80]
}
df = pd.DataFrame(data)
print(df.iloc[0:2])

#Filter Records Based on a Condition

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Marks': [85, 90, 75, 80]
}
df = pd.DataFrame(data)
print(df[df['Marks'] > 80])

#Apply Multiple Conditions

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Age': [20, 21, 19, 22],
    'Marks': [85, 90, 75, 80]
}
df = pd.DataFrame(data)
print(df[(df['Marks'] > 80) & (df['Age'] > 20)])

#Sort Data in Ascending Order

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Marks': [85, 90, 75, 80]
}
df = pd.DataFrame(data)
print(df.sort_values(by='Marks'))

#Sort Data in Descending Order

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Marks': [85, 90, 75, 80]
}
df = pd.DataFrame(data)
print(df.sort_values(by='Marks', ascending=False))
