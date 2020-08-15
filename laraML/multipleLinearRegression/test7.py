import pandas as pd
import math
from sklearn.linear_model import LinearRegression

ds = pd.read_csv('/home/aamir/Desktop/datasets/multivarients.csv')
br = ds.bedroom.median()
all_br = ds.bedroom.fillna(math.floor(br))
ds.bedroom = all_br

reg = LinearRegression()
reg.fit(ds[['area', 'bedroom', 'age']], ds.price)

coefs = reg.coef_
m1 = coefs[0]
m2 = coefs[1]
m3 = coefs[2]
c = reg.intercept_
# predict values for below data
area, bedroom, price = 1400, 3, 4
pre_predict = m1*area + m2*bedroom + m3*price + c
print(pre_predict)
