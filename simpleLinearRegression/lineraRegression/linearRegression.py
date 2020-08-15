"""simple linear regression because only single independent variable.

"""
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([2, 40, 85, 150, 350])
y = np.array([200, 400, 900, 1600, 4000])

x2d = x.reshape(-1, 1)
reg = LinearRegression()
reg.fit(x2d, y)  # independent var always 2d # training system
print(reg.coef_, "coefficient", type(reg.coef_))
print(reg.intercept_, "intercept", type(reg.intercept_))

# y = mx + c # what is the value of y for a given x value
# c is constant/interception value
# m is coef/slope
# on the basis of c and m we can find y
