import numpy as np
# median is the central value of a (sorted) dataset
fields = [7, 5, 4, 2, 1, 8, 3, 6, 9]
median_val = np.median(fields)
print(median_val)

# what if we have even number of values in a dataset
# Two central_values say (x and y) are added & divided dy 2 => x+y/2


fields = [7, 5, 4, 2, 2, 1, 8, 3, 6, 9]
# [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
# (5+4)/2 = 4.5
median_val2 = np.median(fields)
print(median_val2) 
print((4+5)/2)
