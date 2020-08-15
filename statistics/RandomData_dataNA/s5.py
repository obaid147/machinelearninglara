from sklearn.preprocessing import StandardScaler
import pandas
# if x and y values are odd from each other like the values in scale.csv
# we need scaling -> (originalValue - mean)/StandardDeviation
dataset = pandas.read_csv("/home/aamir/Desktop/datasets/scale.csv")
standard_scale = StandardScaler()

scaled_values = standard_scale.fit_transform(dataset)
