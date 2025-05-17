#Logistic distribution is a way to describe how things grow or spread.
#  It’s often used in machine learning, especially in logistic regression and neural networks.
# parameters:It has three main settings:
#loc (mean): This is the center of the distribution, where most values are found.
# scale (spread): This controls how wide or flat the distribution is. A higher value means a flatter curve.
# size: This decides how many random values to generate.
#  uses:: logistic Regression (binary classification problems)
# Neural Networks (activation functions like sigmoid)
# Growth Models (population growth, disease spread)
# Economics & Finance (stock price changes, income distribution)

from numpy import random
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000), hist=False)  # Draw logistic curve
plt.show()
# comparison with normal disrtibution
# Similarities: Both have a bell-shaped curve.
# Differences: The logistic distribution has fatter tails,
#  meaning it predicts extreme values more often than the normal distribution.
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()
