import pandas as pd
import math

ds = pd.read_csv('/home/aamir/Desktop/datasets/multivarients.csv')
br = ds.bedroom.median()
all_br = ds.bedroom.fillna(math.floor(br))
"""
In order to fill some missed data in a column
Find the median of the column and then use fillna
"""
print(all_br)
