#The Chi-Square Distribution is used in statistics to test if data matches what we expect.
#✅ Used to compare actual vs. expected results 📊
# Larger values = bigger differences from expected
#  Common in hypothesis testing (e.g., Chi-Square Test)
#  Used in genetics, surveys, and quality control
# Finding relationships between two things
#Higher Chi-Square value = More difference from expectations
#  (e.g., "Do people who exercise daily eat healthier?")
#💡 Example:
# Imagine you survey 100 people about their favorite color:
# Expected results (equal preference): 25 like Red, 25 like Blue, 25 like Green, 25 like Yellow.
# Actual results: 20 like Red, 30 like Blue, 22 like Green, 28 like Yellow.
# Chi-Square helps us check if these differences happened by chance or mean something important.
#χ =∑ (O−E)^2/E
#Main Parameters
#  df (degrees of freedom) → Controls the shape of the distribution.
# More categories = Higher df = More spread-out distribution.
# size → The number of values we want to generate.
# The graph starts near zero and extends to the right,
#  meaning small differences are common, but large differences are rare
from numpy import random
x = random.chisquare(df=2, size=(2, 3))
print(x)
import matplotlib.pyplot as plt
import seaborn as sns
# Generate 1000 Chi-Square values
sns.histplot(random.chisquare(df=1, size=1000), kde=True)
plt.show()
