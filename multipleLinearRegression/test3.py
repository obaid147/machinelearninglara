import pandas as pd
import math
""" * MEDIAN --> median()
Median --> is a value separating the higher half 
           from the lower half of a data sample (multivarients.csv)
"""
ds = pd.read_csv('/home/aamir/Desktop/datasets/multivarients.csv')
br = ds.bedroom.median()
print(br)  # float value
print(math.floor(br))  # convert float to int
print(int(br))
