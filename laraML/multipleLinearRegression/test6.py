import pandas as pd
import math
from sklearn.linear_model import LinearRegression

ds = pd.read_csv('/home/aamir/Desktop/datasets/multivarients.csv')
br = ds.bedroom.median()
all_br = ds.bedroom.fillna(math.floor(br))
ds.bedroom = all_br

reg = LinearRegression()
reg.fit(ds[['area', 'bedroom', 'age']], ds.price)
# y = m1*area + m2*bedroom + m3*age + c
# m1 coefficient of area, m2 coefficient of bedroom, m3 coefficient of age
print(reg.coef_)
print(reg.intercept_)

