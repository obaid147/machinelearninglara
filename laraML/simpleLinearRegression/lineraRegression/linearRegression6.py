import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

ds = pd.read_csv('/home/aamir/Desktop/datasets/price_area_building.csv')
print(ds)

reg = LinearRegression()
reg.fit(ds[['area']], ds.price)  # training data
# reg.fit(2darray, ds.price)

test_area = np.array([500, 1100, 1600, 2200, 2800, 4000])

test_area2d = test_area.reshape(len(test_area), 1)
# test_area2d = test_area.reshape(-1, 1)

print("Predicted price")
j = 0
for i in reg.predict(test_area2d):
    while j <= 5:
        print("for area {} sqFT, predicted price = {} rupees"
              . format(test_area[j], i))
        j += 1
        break
