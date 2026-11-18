#Read CSV file  
import pandas as pd
df = pd.read_csv('students.csv')
print(df)

#Display First 5 Rows

import pandas as pd
df = pd.read_csv('students.csv')
print(df.head())

#Display Last 5 Rows

import pandas as pd
df = pd.read_csv('students.csv')
print(df.tail())

#Check Number of Rows and Columns

import pandas as pd
df = pd.read_csv('students.csv')
print("\nShape of Dataset:")
print(df.shape)

#Display Column Names

import pandas as pd
df = pd.read_csv('students.csv')
print(df.columns)

#Check Data Types

import pandas as pd
df = pd.read_csv('students.csv')
print(df.dtypes)

#Display Dataset Information

import pandas as pd
df = pd.read_csv('students.csv')
df.info()

#Statistical Summary

import pandas as pd
df = pd.read_csv('students.csv')
print(df.describe())

