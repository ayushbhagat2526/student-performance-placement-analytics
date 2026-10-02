import pandas as pd 

df = pd.read_csv("data/students.csv")
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)