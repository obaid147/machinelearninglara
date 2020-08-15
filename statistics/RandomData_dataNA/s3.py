import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(4, 5, 20)
print(x)

plt.hist(x, 8)
plt.show()

