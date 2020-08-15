import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 10.0, 30)
print(x)
plt.hist(x, 5)
plt.show()
