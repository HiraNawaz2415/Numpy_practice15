#The Pareto Distribution follows Pareto’s Law (80/20 Rule), which means:
# A small number of things contribute to most of the results.
#Where is it used?
# Wealth distribution – A few rich people own most of the money.
#  Business sales – A few products generate most of the revenue.
#  Social media – A few users create most of the content.
#  Natural events – A few big earthquakes cause most destruction.
# Common in economics, business, and social trends
# 20% of people own 80% of the wealth.
#  20% of customers bring 80% of sales.
#  20% of bugs cause 80% of software problems.
# This pattern is what the Pareto Distribution describes.
#It has two parameters:
#  a (alpha - shape parameter) – Controls how extreme the distribution is.
# If a is small, a few things dominate most of the outcome.
# If a is large, things are more evenly spread.
# size – The number of values to generate.
from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)
import matplotlib.pyplot as plt
import seaborn as sns

# Generate 1000 Pareto-distributed values
sns.histplot(random.pareto(a=2, size=1000), kde=True)

plt.show()

