# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Define function
def f(x):
    return 1/x

# Create x and y arrays
x = np.setdiff1d(np.linspace(-10, 10, 100), [0]) # Exclude 0 from x values
y = f(x)

# Plot the function
plt.plot(x, y, label='f(x) = 1/x')

# Add labels, title and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x) = 1/x')
plt.legend()

# Show the plot
plt.show()
