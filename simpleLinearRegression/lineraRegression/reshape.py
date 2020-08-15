import numpy as np

x = np.array([1, 2, 3, 4, 5])
# x = np.array([[1, 2, 3, 4, 5], [100, 200, 1, 2, 3]])
y = np.array([10, 20, 30, 40, 50])
print("#"*10, "Dimensions Before Reshape", "#"*10)
print(x.ndim)
print(y.ndim)
# convert 1D array into 2D array
# reshaping with all the elements of array by adding one more dimension
#               ele, addDim
x2d = x.reshape(len(x), 1)
y2d = x.reshape(len(y), 1)

print(x2d)
print(y2d)
print("#"*10, "Dimensions After Reshape", "#"*10)
print(x2d.ndim)
print(y2d.ndim)


