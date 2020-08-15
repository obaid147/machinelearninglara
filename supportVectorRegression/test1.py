import pandas as pd

data_set = pd.read_csv('/home/aamir/Desktop/datasets/position_salaries.csv')

x = data_set.iloc[:, 1:-1].values
y = data_set.iloc[:, -1].values
print(data_set)
print("--"*40)
print(x)
print("--"*40)
print(y)
print("--"*40)
y = y.reshape(len(y), 1)
print(y)
print("--"*40)
y1 = data_set.iloc[:, 2:3].values
print(y1)
