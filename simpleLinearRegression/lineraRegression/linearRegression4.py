import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('/home/aamir/Desktop/datasets/price_area_building.csv')
print(ds)

# plt.scatter(ds.area, ds.price)
plt.plot(ds.area, ds.price, color='pink', marker="+")
# marker is over blue scatter points if plt.scatter is used
# plt.scatter/plot(column1Name, column2Name) from csv file
plt.xlabel("Area in sqFt's")
plt.ylabel("Price in rupees")
plt.show()
