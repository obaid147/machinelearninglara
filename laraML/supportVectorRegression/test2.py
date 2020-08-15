import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

data_set = pd.read_csv('/home/aamir/Desktop/datasets/position_salaries.csv')

x = data_set.iloc[:, 1:-1].values
y = data_set.iloc[:, -1].values
y = y.reshape(len(y), 1)

sc_X = StandardScaler()
sc_Y = StandardScaler()
x = sc_X.fit_transform(x)
y = sc_Y.fit_transform(y)


regressor = SVR(kernel='rbf')
regressor.fit(x, y)

pred_y = sc_Y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])))
print(pred_y)
pred_y = sc_Y.inverse_transform(regressor.predict(sc_X.transform([[11.5]])))
print(pred_y)
