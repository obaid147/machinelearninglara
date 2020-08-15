import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([2, 40, 85, 150, 350])
y = np.array([200, 400, 900, 1600, 4000])

x2d = x.reshape(-1, 1)
# -1 or len(x) both means use all elements of x as it is
# 1 means add one more dimensions
reg = LinearRegression()
reg.fit(x2d, y)  # giving data for training the LinearRegression System

plt.scatter(x, y)  # points / dots
plt.plot(x, reg.predict(x2d))  # intercepting line
# this line would be at least distance from every point
plt.show()
