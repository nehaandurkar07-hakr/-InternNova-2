#Identify Missing Values

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Marks': [85, None, 75, None]
}
df = pd.DataFrame(data)
print(df.isnull())
print("\n")


#Count Missing Values

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Marks': [85, None, 75, None]
}
df = pd.DataFrame(data)
print(df.isnull().sum())
print("\n")


#Remove Missing Values

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Marks': [85, None, 75, None]
}
df = pd.DataFrame(data)
new_df = df.dropna()
print(new_df)
print("\n")

#Fill Missing Values

import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Marks': [85, None, 75, None]
}
df = pd.DataFrame(data)
df['Marks'] = df['Marks'].fillna(0)
print(df)

