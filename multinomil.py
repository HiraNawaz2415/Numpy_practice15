#The Multinomial Distribution is a way to describe the probability of different outcomes when you repeat an experiment multiple times, and each trial has more than two possible results.
# Think of it as an extension of the Binomial Distribution,
#  which deals with only two outcomes (like heads or tails in a coin toss). 
# Instead of just two outcomes, the Multinomial Distribution works for three or more.
#Used when there are more than two possible outcomes per trial.
#  Tracks how many times each outcome happens.
#  Useful for problems like rolling dice, choosing colors, elections, genetics, and language processing.
#Think of it as rolling a dice. A dice has six faces (1, 2, 3, 4, 5, 6), 
# Blood types in a population, where each person has a blood type (A, B, AB, O).
# so each time you roll it, there are six possible outcomes, not just two.
# it has three parameters::
#1️ n (Number of Trials) → How many times you do the experiment (e.g., roll a dice 6 times).
#pvals (Probabilities) → A list of probabilities for each outcome (e.g., for a fair dice, each number has a 
#  size (Shape of Output)
from numpy import random

# Rolling a dice 6 times (each number has a 1/6 probability)
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

#his will not return a single value (like just one number).
#  Instead, it returns a list showing how many times each outcome appeared.
# For example, the output might look like this:
# [1 2 0 1 1 1]
# This means:
# 1 time we got a "1"
# 2 times we got a "2"
# 0 times we got a "3"
# 1 time we got a "4"
# 1 time we got a "5"
# 1 time we got a "6"
