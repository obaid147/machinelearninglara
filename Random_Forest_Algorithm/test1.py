import pandas as pd

data_set = pd.read_csv('/home/aamir/Desktop/datasets/position_salaries.csv')
x = data_set.iloc[:, 1:-1].values
y = data_set.iloc[:, -1].values

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=10, random_state=85)
regressor.fit(x, y)

predict_y = regressor.predict([[6.5]])
print(predict_y)
