import pandas as pd
import matplotlib.pyplot as plt
"""  Parabolic shape-------------------
    when trained data produces / plots a curve it's polynomial regression.
    Through scatter points / plot we can find if it's linear or polynomial reg. 
    we cannot find best-fit straight line we can find best-fit curved line.
"""
ds = pd.read_csv('/home/aamir/Desktop/datasets/exp-sal.csv')

x = ds.iloc[:, 0:1]  # every row : rows of first column
y = ds.iloc[:, 1:2]  # every row : rows of second column


plt.title("Experience-Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.scatter(x, y, edgecolors='yellow', markersize=5)

plt.plot(x, y, color='purple')

plt.show()
"""
plt.scatter(x,y, s=500, marker='s', edgecolor='black', linewidth=3, facecolor='green', hatch='|')
# compare with no borders, and denser hatch.
plt.subplot(122)
plt.scatter(x,y2, s=500, marker='s', edgecolor='black', linewidth=0, facecolor='green', hatch='||||'
"""
