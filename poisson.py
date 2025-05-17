# The Poisson distribution helps us predict how often something will happen in a fixed period of time or space if we know the average rate at which it happens.
# discrete probability distribution
#Examples:
# How many emails you get per day if you usually get 10.
# How many calls a customer service center gets in an hour.
# How many raindrops fall on a specific spot in 10 minutes.
# "How many customers will visit a shop in an hour?"
#  "How many messages will I receive in 5 minutes?"
#  "How many people will enter a hospital emergency room in a day?"
# it has two parasmmerters
#Lambda (lam) → Average Rate of Events
#he average number of times an event happens in a fixed period of time or space.
#Size → Shape of the Output Data how many random numbers we want to generate.
from numpy import random
# Simulate customer arrivals in a bakery (average 5 per hour)
x = random.poisson(lam=5, size=10)
print(x)  # Example output: [3, 5, 4, 6, 2, 5, 7, 3, 5, 6]
# Generate a 3x3 matrix of Poisson-distributed numbers (lam=4)
x = random.poisson(lam=4, size=(3,3))
print(x)
import matplotlib.pyplot as plt
import  seaborn as sns
sns.displot(random.poisson(lam=5,size=10))
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Generate Poisson data (λ=5, 1000 samples)
data = random.poisson(lam=5, size=1000)

# Plot the distribution
sns.histplot(data, bins=10, kde=False)
plt.xlabel("Number of Customers per Hour")
plt.ylabel("Frequency")
plt.title("Poisson Distribution (λ=5)")
plt.show()
