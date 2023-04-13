import random
import matplotlib.pyplot as plt

results = []
for i in range(600):
    random_numbers = [random.randint(1, 6) for _ in range(i+1)]
    average = sum(random_numbers) / len(random_numbers)
    results.append(average)

plt.plot(results)
plt.xlabel('Number of Dice rolls')
plt.ylabel('Average')
plt.show()
