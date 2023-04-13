# Import libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

# Define function
def f(x):
    return 1/x

# Create x and y arrays
x = np.setdiff1d(np.linspace(-10, 10, 100), [0]) # Exclude 0 from x values
y = f(x)

# Calculate y' array using scipy.misc.derivative
y_prime = misc.derivative(f, x)

# Plot both functions
plt.plot(x, y, label='f(x) = 1/x')
plt.plot(x, y_prime, label="f'(x) = -1/x^2")

# Add labels, title and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x) = 1/x and its derivative')
plt.legend()

# Show the plot
plt.show()

