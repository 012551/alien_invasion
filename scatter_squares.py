import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, edgecolors='none', s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis='both', which='major', labelsize=14)
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.show()
