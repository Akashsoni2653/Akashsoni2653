import matplotlib.pyplot as plt

numbers = range(1, 1000001)
squared_numbers = [x**2 for x in numbers]

plt.plot(numbers, squared_numbers)
plt.xlabel("Number")
plt.ylabel("Square of Number")
plt.show()
