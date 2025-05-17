#Uniform Distribution is a type of probability distribution 
# where every value within a given range has an equal chance of occurring.
# like rolling a fair die:Each number (1, 2, 3, 4, 5, or 6) has an equal probability of being rolled.
# the Uniform Distribution is defined by three parameters:
#low (minimum value) → The starting value of the range.Default: 0.0
# high (maximum value) → The ending value of the range.Default: 1.0
# size → Defines how many random numbers (samples) should be generated.
# Can be a single number or an array shape (e.g., (2,3) for a 2-row, 3-column array).
from numpy import random
# Generate a 2x3 array of random numbers
x = random.uniform(size=(2, 3))
print(x)

# Set custom range
low = 5    # Minimum value
high = 15  # Maximum value

# Generate a single random number
single_value = random.uniform(low, high)
print("Single Random Value:", single_value)

# Generate an array of 5 random numbers
array_values = random.uniform(low, high, size=5)
print("Array of Random Values:", array_values)
import matplotlib.pyplot as plt
import seaborn as sns

# Generate 1000 samples from a uniform distribution between 5 and 15
data = random.uniform(5, 15, 1000)

# Plot the distribution
sns.histplot(data, bins=30, kde=True, color='blue')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Uniform Distribution (Low=5, High=15)")

plt.show()
