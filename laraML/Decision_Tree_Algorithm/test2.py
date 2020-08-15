import pandas as pd
from sklearn.preprocessing import LabelEncoder


data_set = pd.read_csv('/home/aamir/Desktop/datasets/company-job-education.csv')
inputs = data_set.drop('salary_more_than_30L_PA', axis='columns')
target = data_set['salary_more_than_30L_PA']


le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

# change to numerics
inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_company.fit_transform(inputs['job'])
inputs['degree_n'] = le_company.fit_transform(inputs['degree'])

print(inputs)
