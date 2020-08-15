import pandas as pd

""" * MEDIAN --> median()
Median --> is a value separating the higher half 
           from the lower half of a data sample (multivarients.csv)
"""
ds = pd.read_csv('/home/aamir/Desktop/datasets/multivarients.csv')
print(ds)

print("area median = ", ds.area.median())
print("bedroom median = ", ds.bedroom.median())
print("age median = ", ds.age.median())
print("price median = ", ds.price.median())

