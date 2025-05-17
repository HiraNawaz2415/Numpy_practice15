#The Zipf Distribution follows a pattern where a few items appear very often, while most items appear rarely.
# This follows Zipf’s Law, which states
#  The 2nd most common item appears half as often as the most common.
#  The 3rd most common appears one-third as often, and so on.
#Where is Zipf Distribution Used?
#  Word Frequency in Languages – A few words (like "the", "is") appear often, while most words are rare.
#  Website Traffic – A few websites (like Google, YouTube) get most of the visitors, while millions of sites get very few.
#  Book Sales – A few books (like Harry Potter) sell millions of copies, while most books sell very few.
#  City Populations – A few cities have huge populations, while most cities are small.
#The Zipf distribution has two parameters:
# a (alpha - distribution parameter) – Controls how big the difference is between common and rare items.
# If a is small, the difference is not very big.
# If a is large, a few items dominate almost completely.
# size – The number of values to generate.

from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.histplot(x[x < 10], kde=False)  # Only plotting values less than 10 for clarity

plt.show()
