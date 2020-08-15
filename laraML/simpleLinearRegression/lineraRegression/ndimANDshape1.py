import numpy as np

x = np.array([1, 2, 3, 4, 5])
# x = np.array([[1, 2, 3, 4, 5], [100, 200, 1, 2, 3]])
y = np.array([10, 20, 30, 40, 50])

# ndim --> number of dimensions
print(x.ndim)
print(y.ndim)

# shape --> number of elements inside array in the form of tuple
print(x.shape)
print(y.shape)
print(type(x.shape))
