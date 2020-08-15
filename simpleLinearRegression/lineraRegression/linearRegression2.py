import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([2, 40, 85, 150, 350])
y = np.array([200, 400, 900, 1600, 4000])

x2d = x.reshape(-1, 1)
# -1 or len(x) both means use all elements of x as it is
# 1 means add one more dimensions

reg = LinearRegression()
reg.fit(x2d, y)  # Getting trained with trained data
m = reg.coef_  # slope
c = reg.intercept_  # constant
predict_y = m * 180 + c  # predict value of y for a given x value
"""
The value of x ie 180 [2, 40, 85, 150, 350] comes between 150 and 350
that means the value of y should be [200, 400, 900, 1600, 4000] between
                                                    1600 and 4000
"""
print(f"Predicted value of y is {predict_y}")
