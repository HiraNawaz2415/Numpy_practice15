#The Normal Distribution (also called Gaussian Distribution) is a bell-shaped curve that appears naturally in many real-life situations.
#Where Do We See Normal Distribution?
# Human Heights – Most people have an average height, fewer are very tall or very short.
#  IQ Scores – Most people have an average IQ, very few have extremely low or extremely high IQ.
#  Heart Rates – Most people have a normal heartbeat, very few have extremely low or high heart rates.
#Properties of Normal Distribution
# Mean (loc) → This is the center of the curve (the average value).
# Standard Deviation (scale) → This controls how spread out the data is.
# Small standard deviation → The curve is narrow and tall (data is close to the mean).
# Large standard deviation → The curve is wide and flat (data is more spread out).
#Default mean = 0, default standard deviation = 1.
#KDE stands for Kernel Density Estimation. 
# It is a method used to smoothly estimate the distribution of a dataset.
from numpy import random
x = random.normal(size=(2, 3))  # Creates a 2x3 array of random values
print(x)
x = random.normal(loc=1, scale=3, size=(2, 3))  # Mean = 1, Std Dev = 2
print(x)
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.normal(size=1000), kde=True)  # kde=True adds a smooth curve
plt.show()
