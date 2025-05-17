#The Binomial Distribution is a discrete probability distribution
#  that models the number of successes in a fixed number of independent trials,
#  each with the same probability of success.
# Two Possible Outcomes
#The outcomes are countable (0, 1, 2, …, n).
# Binomial Distribution is a way to describe the probability of getting a certain number of successes in a fixed number of trials, 
# where each trial has only two possible outcomes:
#It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
#Fixed Number of Trials (n):predetermined.
#Constant Probability (p):
#probability of success remains the same across trials.
#Independent Trials: The outcome of one trial does not affect another.
#Use Cases
# Coin Tossing: Probability of getting exactly 3 heads in 5 coin flips.
# Quality Control: Finding the probability that a batch of 10 products contains 2 defective items.
# Medical Trials: Probability that exactly 7 out of 10 patients recover from a treatment.
# Marketing: Probability that 4 out of 100 customers buy a product.


# It Has Three Parameters
# n (number of trials) → Total number of times the experiment is repeated.
# p (probability of success) → Chance of success in each trial (e.g., for a fair coin, p = 0.5).
# size (sample size) → How many times you want to simulate the experiment.
from numpy import random
x = random.binomial(n=10, p=0.5, size=10)
print(x)
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=100), hist=True, kde=False)
plt.show()
# Difference bewteen:
sns.kdeplot(random.normal(loc=50, scale=5, size=1000), label="Normal", linestyle="dashed")
sns.kdeplot(random.binomial(n=100, p=0.5, size=1000), label="Binomial")

plt.legend()
plt.show()
