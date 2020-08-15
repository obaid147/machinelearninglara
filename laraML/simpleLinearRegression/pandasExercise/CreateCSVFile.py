import pandas
area = [10, 20, 30, 45, 70, 90]
price = [50, 100, 150, 225, 400, 550]
dictionary = {'area': area, 'price': price}

df = pandas.DataFrame(dictionary)

df.to_csv(r'Home\aamir\Desktop\datasets\data2.csv', index=False)

z = pandas.read_csv(r"Home\aamir\Desktop\datasets\data2.csv")
print(z)