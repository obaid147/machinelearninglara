from scipy import stats

# mode method is in scipy package and not in numpy
fields = [7, 5, 4, 100, 2, 1, 8, 3, 100, 6, 9]
# number in a dataset that is repeating more times is the mode.
mode_val = stats.mode(fields)
print(mode_val)

# if a dataset has none repeating elements then the dataset has no mode and returns 1 as mode
# and count

# bimodal when dataset contains two elements repeating.
# trimodal when dataset contains three elements repeating.
# multimodal when dataset contains more than 4 elements repeating.



