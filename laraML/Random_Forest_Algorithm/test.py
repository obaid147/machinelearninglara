import pandas as pd

data_set = pd.read_csv('/home/aamir/Desktop/datasets/position_salaries.csv')
x = data_set.iloc[:, 1:-1].values
y = data_set.iloc[:, -1].values

from sklearn.ensemble import RandomForestRegressor

reg = RandomForestRegressor(n_estimators=10, random_state=0)
reg.fit(x, y)

predict_y = reg.predict([[6.5]])
print(predict_y)