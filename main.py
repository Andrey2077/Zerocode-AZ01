import pandas as pd

data = pd.read_csv('glass.csv')
print(data.head())
print(data.info())
print(data.describe())

data_salary = pd.read_csv('dz.csv')
# print(data_salary)
data_salary['City'] = data_salary['City'].fillna(' ')
data_salary['Salary'] = data_salary['Salary'].fillna(0)
# data_salary['Salary'].fillna(0, inplace=True)
print(data_salary)
group = data_salary.groupby('City')['Salary'].mean()
print(group)