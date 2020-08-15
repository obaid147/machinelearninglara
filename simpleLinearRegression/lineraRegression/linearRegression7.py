import pandas as pd
from sklearn.linear_model import LinearRegression

ds = pd.read_csv('/home/aamir/Desktop/datasets/price_area_building.csv')
reg = LinearRegression()
reg.fit(ds[['area']], ds.price)  # training data

ds = pd.read_csv('/home/aamir/Desktop/datasets/test_area_price.csv')
resulted_price = reg.predict(ds[['area']])
print(resulted_price)