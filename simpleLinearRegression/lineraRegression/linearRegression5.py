import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

ds = pd.read_csv('/home/aamir/Desktop/datasets/price_area_building.csv')
print(ds)

reg = LinearRegression()
reg.fit(ds[['area']], ds.price)  # training data
# reg.fit(2darray, ds.price)

plt.scatter(ds.area, ds.price)
plt.plot(ds.area, reg.predict(ds[['area']]))  # linearReg's predict
plt.show()
