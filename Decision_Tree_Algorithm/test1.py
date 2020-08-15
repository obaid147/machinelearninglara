import pandas as pd
data_set = pd.read_csv('/home/aamir/Desktop/datasets/company-job-education.csv')
print(data_set)
print("*"*50)

inputs = data_set.drop('salary_more_than_30L_PA', axis='columns')
target = data_set['salary_more_than_30L_PA']
print(inputs)
print()
print("*"*20 + '\nTARGET')
print(target)
