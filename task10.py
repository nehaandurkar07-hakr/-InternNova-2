
import pandas as pd

# Creating Dataset
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha', 'Riya', 'Karan'],
    'Department': ['IT', 'CS', 'IT', 'CS', 'IT', 'CS'],
    'Maths': [85, 90, 75, 80, 95, 70],
    'Science': [80, 95, 70, 85, 90, 75]
}

df = pd.DataFrame(data)

# 1. Display Dataset
print("Original Dataset:")
print(df)

# 2. Inspect Dataset
print("\nDataset Information:")
print(df.info())

print("\nDataset Description:")
print(df.describe())

# 3. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Handle Missing Values
df = df.fillna(0)

# 5. Select Data
print("\nSelected Columns:")
print(df[['Name', 'Maths']])

# 6. Filter Data
print("\nStudents with Maths Marks Above 80:")
print(df[df['Maths'] > 80])

# 7. Sort Data
print("\nSorted Data:")
print(df.sort_values(by='Maths', ascending=False))

# 8. GroupBy Analysis
print("\nDepartment Wise Average:")
print(df.groupby('Department')[['Maths', 'Science']].mean())

# 9. Pivot Table
print("\nPivot Table:")
print(pd.pivot_table(
    df,
    values='Maths',
    index='Department',
    aggfunc='mean'
))

# 10. Find Insights
print("\nHighest Maths Marks:")
print(df['Maths'].max())

print("\nAverage Maths Marks:")
print(df['Maths'].mean())

# 11. Export Dataset
df.to_csv('student_performance.csv', index=False)

print("\nDataset Exported Successfully!")
