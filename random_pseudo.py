# Random numbers: the number is generated in a way that no pattern can be identified.
#Pseudo Random vs. True Random
#Computers work using programs, and programs follow a set of fixed instructions. 
# This means that when a computer generates a random number,
#  it is actually following a set of rules (an algorithm) to do so.
#Since we can figure out (predict) how the number is generated, it is called a pseudo-random number (fake random number).
#true random numbers are generated from real-world events, such as:
#✔ Keystrokes (when you type on your keyboard)
#✔ Mouse movements
#✔ Network data (random data from the internet)
#Pseudo-random numbers are generated using an algorithm and can be predicted.
#True random numbers come from real-world events and are used in security.
#NumPy provides the random module to generate:
# Random integers with randint()
# Random floats with rand()
# Random arrays with randint(size=()) and rand(size=())
# Random selections from a given list with choice()
from numpy import random
# Generating random numbers
print("Random random numbers::")
x = random.randint(100)  # Generates a random integer between 0 and 99
print(x) # This will generate different numbers each time run it
#Generating a Random Floating-Point Number
#To generate a random float between 0 and 1, we use rand()
x = random.rand()  # Generates a random float between 0 and 1
print("Floating point random numbers::")
print(x)

#Generating an Array of Random Integers
x = random.randint(100, size=(5))  # Generates 5 random integers
print("In 1D int array")
print(x)
#To create a 2D array (like a table with rows and columns):
x = random.randint(100, size=(3, 5))  # 3 rows, 5 columns
print("In 2D int array")
print(x)

#Generating an Array of Random Floats
x = random.rand(5)  # 1D array with 5 random float numbers
print("In 1D float array")
print(x)
#For a 2D array of floats:
print("In 2D float array")
x = random.rand(3, 5)  # 3 rows, 5 columns
print(x)
#Selecting a Random Value from an Array
x = random.choice([3, 5, 7, 9])  # Picks one random value from the list
print(x)

#Generating an Array of Random Choices
x = random.choice([3, 5, 7, 9], size=(3, 5))  # 3 rows, 5 columns
print(x)

