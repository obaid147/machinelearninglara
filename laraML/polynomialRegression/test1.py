import pandas as pd
import matplotlib.pyplot as plt
"""
    when trained data produces / plots a curve it's polynomial regression.
    Through scatter points / plot we can find if it's linear or polynomial reg. 
    we cannot find best-fit straight line we can find best-fit curved line.
"""
ds = pd.read_csv('/home/aamir/Desktop/datasets/exp-sal.csv')

x = ds.iloc[:, 0:1]  # every row : rows of first column
y = ds.iloc[:, 1:2]  # every row : rows of second column
plt.scatter(x, y)
plt.show()
