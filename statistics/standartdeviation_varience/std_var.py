import numpy as np
import math

# np.std-> how far or how close the members of a dataset are
# Its symbol is σ (the greek letter sigma)
# it is the square root of the Variance.
# The average of the squared differences from the Mean.

field = [28, 29, 30, 31, 32]
# in-build methods
var_val = np.var(field)
print('variance', var_val)
std_val = np.std(field)
print('Standard deviation', std_val)

# Steps to find numpy.var then numpy.std
# 1. find mean
sd_mean_val = np.mean(field)

new_filed = []
# 2 (field_val - mean)^2
for i in field:
    val = (i - sd_mean_val)**2
    new_filed.append(val)

# 3 sum of new_field values
sum_new_field = sum(new_filed)

# 4 (sum of new_field values) / length of dataset N
var = sum_new_field/len(field)

# 5 variance
print('variance ', var)

# 5 squareRoot of step 4 => std
sd = math.sqrt(var)
print('Standard deviation', sd)
