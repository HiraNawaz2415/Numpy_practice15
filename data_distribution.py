#Data distribution tells us how often values appear in a dataset.
# We can generate random numbers that follow specific probabilities using NumPy’s random.choice().
# Each value is assigned a probability (between 0 and 1) that determines how often it appears.
# The sum of all probabilities must be 1.
# We can generate single values, 1D arrays, or 2D arrays with this method.
#What is a Random Distribution?
# A random distribution is a collection of random numbers that follow a specific pattern or rule.
#In statistics, we use something called a Probability Density Function (PDF) to describe how likely different values are to appear in our data.
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
#his will generate 100 random numbers,
#  but you will never see the number 9 in the output because its probability is set to 0.
#Create a 2D Array of Random Numbers
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.0, 0.6], size=(100))
print(x)

# Random permutation
#A permutation means changing the order of elements in a list or array.
#For example:
#👉 [1, 2, 3] can be rearranged as [3, 2, 1], [2, 1, 3], etc.
#NumPy Random module provides two methods for creating random permutations:
#shuffle() – Changes the order of elements in the original array.
# permutation() – Creates a new array with elements rearranged but does not modify the original one.
#Shuffle an Array

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print("After shuffling::")
print(arr)

#Generate a Random Permutation
arr = np.array([1, 2, 3, 4, 5])
new_arr = random.permutation(arr)
print("After permutation new array")
print(new_arr)  # New shuffled array
print(arr)      # Original array remains unchanged
