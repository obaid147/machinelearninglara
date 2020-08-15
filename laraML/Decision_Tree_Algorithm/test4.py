import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree


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

inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')
# print(inputs_n)

model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)
pred_v = model.predict([[1, 2, 0]])
print(pred_v)

pred_v = model.predict([[2, 2, 1]])
print(pred_v)