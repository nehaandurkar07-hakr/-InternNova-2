#Export DataFrame to CSV

import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 75]
}

df = pd.DataFrame(data)

df.to_csv('students_output.csv', index=False)

print("\nData exported successfully!")

#Verify Exported CSV File

import pandas as pd

df = pd.read_csv('students_output.csv')

print("\nExported Data:")
print(df)
