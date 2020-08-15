import math

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

ds = pd.read_csv('/home/aamir/Desktop/datasets/exp-sal.csv')

x = ds.iloc[:, 0:1]
y = ds.iloc[:, 1:2]

poly = PolynomialFeatures(degree=2)  # default
linear_reg = LinearRegression()

poly_x = poly.fit_transform(x)
linear_reg.fit(poly_x, y)

plt.scatter(x, y)
pred_y = linear_reg.predict(poly.fit_transform([[13]]))
#  predicting salary of person with 13 years of experience.
print(math.floor(pred_y))
