import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
a = 150
b = 180

# Define the CDF function
def uniform_cdf(x, a, b):
    if x < a:
        return 0
    elif x >= b:
        return 1
    else:
        return (x - a) / (b - a)

# Generate x values for plotting
x_values = np.linspace(140, 190, 1000)
cdf_values = [uniform_cdf(x, a, b) for x in x_values]

# Plot the CDF
plt.figure(figsize=(10, 6))
plt.plot(x_values, cdf_values, label='CDF', color='green')
plt.title('Cumulative Distribution Function (CDF) for Uniform Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Cumulative Probability')
plt.axvline(x=a, color='grey', linestyle='--', label='a (min)')
plt.axvline(x=b, color='grey', linestyle='--', label='b (max)')
plt.legend()
plt.grid(True)
plt.show()
