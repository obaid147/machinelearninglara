import matplotlib.pyplot as plt

age = [23, 34, 45, 60, 75]
running_speed = [100, 70, 50, 30, 10]
plt.plot(age, running_speed)
plt.scatter(age, running_speed, edgecolors='red')
# as age is increasing, running_speed is decreasing
plt.show()  # all points are scatter plot
#  regression is nothing but relation, how points can be scattered
# ie x and y ==> age and speed
# point is the meeting place of two values

