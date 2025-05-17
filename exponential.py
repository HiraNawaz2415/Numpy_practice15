#The Exponential Distribution helps us understand the time between random events 
# that happen continuously.
#How long will I have to wait until something happens?"
#It is commonly used to model:
# Waiting time for a bus (When will the next bus arrive?)
#  How long a light bulb will last (When will it burn out?)
#  Time between customer arrivals (When will the next person enter a shop?)
#  Time between earthquakes (When will the next earthquake happen?)
#How It Works
# Events happen at a constant average rate, but the exact time between them is random.
# for example, if a bus arrives every 5 minutes on average, 
# sometimes it may come in 2 minutes, sometimes in 7 minutes, but over time,
#  the average waiting time is still 5 minutes.
#Main Parameters
# scale (λ or lambda) → The average time between events.
#  Example: If scale = 2, the event happens every 2 time units on average.
# size → The shape of the output (how many numbers you want).
#Let's say an event happens every 2 minutes on average, and we want a 2×3 matrix of random waiting times:
from numpy import random

# Generate waiting times
x = random.exponential(scale=2, size=(2, 3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

# Generate 1000 random numbers and plot the distribution
sns.histplot(random.exponential(size=1000), kde=True)

plt.show()

