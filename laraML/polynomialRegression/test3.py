import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

"""
In case of Linear we do not need to transform independent variables.
In case of Polynomial we need to transform independent variables.
"""
ds = pd.read_csv('/home/aamir/Desktop/datasets/exp-sal.csv')

x = ds.iloc[:, 0:1]
y = ds.iloc[:, 1:2]

# poly = PolynomialFeatures(degree=6)
poly = PolynomialFeatures(degree=2)  # default
linear_reg = LinearRegression()

poly_x = poly.fit_transform(x)  # convert ordinary x value to polynomial x values
linear_reg.fit(poly_x, y)

plt.scatter(x, y)
plt.plot(x, linear_reg.predict(poly_x))
plt.show()
