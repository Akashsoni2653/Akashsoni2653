import random
import matplotlib.pyplot as plt

results = []
for i in range(1, 40001):
    numbers = [random.randint(1, 6) for _ in range(i)]
    average = sum(numbers) / len(numbers)
    results.append(average)
    print(f"After {i} rolls, the average is {average}")

plt.plot(results)
plt.xlabel("Number of Rolls")
plt.ylabel("Average")
plt.show()
