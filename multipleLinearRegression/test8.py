import pandas as pd
import math
from sklearn.linear_model import LinearRegression

ds = pd.read_csv('/home/aamir/Desktop/datasets/multivarients.csv')
br = ds.bedroom.median()
all_br = ds.bedroom.fillna(math.floor(br))
ds.bedroom = all_br

reg = LinearRegression()
reg.fit(ds[['area', 'bedroom', 'age']], ds.price)

predict_price = reg.predict([[1400, 3, 4]])
print(predict_price)
