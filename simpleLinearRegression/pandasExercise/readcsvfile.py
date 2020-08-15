import pandas as pd

data_set = pd.read_csv('/home/aamir/Desktop/datasets/person.csv', index=False)
print(data_set)  # all rows and columns
print("#" * 10)
# print(data_set.iloc[rows, cols])
print(data_set.iloc[:, :])  # all rows and columns
# iloc --> index location
print("#" * 10)

print(data_set.iloc[0:1, :])  # ist row by index
print("#" * 10)

print(data_set.iloc[1:2, :])  # index 1 to index 2, 2 is exclusive
print("#" * 10)

print(data_set.iloc[2:3, :])  # from 1 to 3, 3 is exclusive
print("#" * 10)

print(data_set.iloc[1:3, :])  # from 1 to 3, 3 is exclusive
print("#" * 10)
# ##############################COLUMNS#############################
# one column value for all rows
print(data_set.iloc[:, :1])  # first column
print("#" * 10)

print(data_set.iloc[:, 1:2])  # 2nd column
print("#" * 10)

print(data_set.iloc[:, 2:3])  # 3nd column
print("#" * 10)

print(data_set.iloc[:, 3:])  # 4nd column
print("#" * 10)
print(data_set.iloc[:, 2:])  # last 2 columns
print("#" * 10)
print(data_set.iloc[0:1, 3:])  # salary of first row
print("#" * 10)
print(data_set.iloc[3:4, 1:3])  # last row and sec and 3rd col

print("#" * 10)
print(data_set.iloc[:, :-1])  # read all columns except last column

print("Using Display")
from IPython.display import display
display(data_set)
