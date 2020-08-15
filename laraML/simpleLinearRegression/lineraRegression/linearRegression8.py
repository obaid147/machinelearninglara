import pandas as pd
from sklearn.linear_model import LinearRegression
ds = pd.read_csv('/home/aamir/Desktop/datasets/price_area_building.csv')
reg = LinearRegression()
reg.fit(ds[['area']], ds.price)  # training data

ds = pd.read_csv('/home/aamir/Desktop/datasets/test_area_price.csv')
predicted_price = reg.predict(ds[['area']])
ds['predicted-price'] = predicted_price
ds.to_csv('/home/aamir/Desktop/datasets/toCSV_test_area_price.csv', index=False)

# exporting predicted price with given areas to new csv file.
