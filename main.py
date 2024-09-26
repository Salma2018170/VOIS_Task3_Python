import pandas as pd
import csv

df = pd.read_csv('Employees.csv')
print(df)
"""
check duplicated colum and remove any duplicated from tabel and  return same  DataFrame  
"""
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df)

"""
- Remove any decimal places in the Age column
"""
df['Age'] = df['Age'].astype(int)
print(df)

"""
-Convert the USD salary to EGP
"""
exchange_rate_usd_to_egp = 48.5
df['Salary(EGP)'] = df['Salary(USD)'] * exchange_rate_usd_to_egp
print(df)

"""
- Average age
- Median Salaries
- Ratio between males and female employees
"""
average_age = df['Age'].mean()
print(int(average_age))

median_salary = df['Salary(USD)'].median()
print(median_salary)

groupby_gender = df.groupby('Gender')['Gender'].count()
print(groupby_gender)

"""
performing the previous steps, write the data in a new CSV file
"""
# print(df)
with open('EmployeesAfterUpdate.csv', 'w') as file:
    writer = csv.writer(file)
    field = ["average_age", "median_salary", "female", "male"]

    writer.writerow(field)
    writer.writerow([int(average_age), int(median_salary), int(groupby_gender['F']), int(groupby_gender['M'])])

df_update = pd.read_csv('EmployeesAfterUpdate.csv')
print(df_update)