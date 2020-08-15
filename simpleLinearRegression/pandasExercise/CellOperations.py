import pandas as pd

data_set = pd.read_csv("/home/aamir/Desktop/datasets/person.csv")
print(data_set)

print("*"*10, '\'Serial Numbers\'', "*"*10)
sno1 = data_set.iloc[0, 0]  # Serial Number 1
sno2 = data_set.iloc[1, 0]  # Serial Number 2
sno3 = data_set.iloc[2, 0]  # Serial Number 3
sno4 = data_set.iloc[3, 0]  # Serial Number 4
print(sno1)
print(sno2)
print(sno3)
print(sno4)
print()

print("*"*10, '\'Names\'', "*"*10)
name1 = data_set.iloc[0, 1]
name2 = data_set.iloc[1, 1]
name3 = data_set.iloc[2, 1]
name4 = data_set.iloc[3, 1]
print(name1)
print(name2)
print(name3)
print(name4)
print()

print("*"*10, '\'Ages\'', "*"*10)
age1 = data_set.iloc[0, 2]
age2 = data_set.iloc[1, 2]
age3 = data_set.iloc[2, 2]
age4 = data_set.iloc[3, 2]
print(age1)
print(age2)
print(age3)
print(age4)
print()

print("*"*10, '\'Salaries\'', "*"*10)
salary1 = data_set.iloc[0, 3]
salary2 = data_set.iloc[1, 3]
salary3 = data_set.iloc[2, 3]
salary4 = data_set.iloc[3, 3]
print(salary1)
print(salary2)
print(salary3)
print(salary4)
print()
