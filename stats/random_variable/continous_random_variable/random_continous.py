import numpy as np
import matplotlib.pyplot as plt

# Define the PDF and CDF for the popcorn example
def pdf(x):
    if 1 <= x <= 5:
        return 0.25  # Uniform distribution between 1 and 5 seconds
    else:
        return 0

def cdf(x):
    if x < 1:
        return 0
    elif 1 <= x <= 5:
        return 0.25 * (x - 1)
    else:
        return 1

# Generate values for plotting
x_values = np.linspace(0, 6, 2000)
print(len(x_values))
pdf_values = np.array([pdf(x) for x in x_values])
cdf_values = np.array([cdf(x) for x in x_values])

# Plot the PDF
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values, pdf_values, label='PDF', color='blue')
plt.fill_between(x_values, pdf_values, color='green', alpha=0.2)
plt.title('Probability Density Function (PDF)')
plt.xlabel('Time (seconds)')
plt.ylabel('Probability Density')
plt.legend()

# Plot the CDF
plt.subplot(1, 2, 2)
plt.plot(x_values, cdf_values, label='CDF', color='red')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Time (seconds)')
plt.ylabel('Cumulative Probability')
plt.legend()

plt.tight_layout()
plt.show()
