import numpy as np
fields = [1, 2, 3, 4, 5, 6, 7]
mean_val = np.mean(fields)
print(mean_val)

# sum of values in dataset / len(dataset)
s = 0
l = len(fields)
for i in fields:
    s += i

mean_val2 = s / l
print(mean_val2)

# both mean_val and mean_val2 are same
