import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 40, 85, 150, 350]) # x is independent
y = np.array([200, 400, 900, 1600, 4000])  # y is dependent on x

plt.scatter(x, y)  # points
plt.plot(x, y)  # line
plt.show()
