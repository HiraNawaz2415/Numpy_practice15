# Filtering in array
#Filtering means selecting specific elements from an array based on certain conditions.
#  The selected elements are used to create a new array.
#  filtering is done using Boolean indexing. This means we create a list of True and False values, where:
#True means we keep that element in the new array.
#False means we remove that element
#  Manually Creating a Filter
arr = np.array([41, 42, 43, 44])
# Boolean list that decides which elements to keep
filter_arr = [True, False, True, False]
# Apply the filter
newarr = arr[filter_arr]
print(newarr)  # Output: [41, 43]
# Creating a Filter Using a Conditio
#  keep only numbers greater than 42.
arr = np.array([41, 42, 43, 44])

# Create a filter list based on a condition
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

# Apply the filter
newarr = arr[filter_arr]
print(filter_arr)  # Output: [False, False, True, True]
print(newarr)  # Output: [43, 44]
# Filtering Even Numbers
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for element in arr:
    if element % 2 == 0:  # Check if the number is even
        filter_arr.append(True)
    else:
        filter_arr.append(False)

# Apply the filter
newarr = arr[filter_arr]
print(filter_arr)  # Output: [False, True, False, True, False, True, False]
print(newarr)  # Output: [2, 4, 6]
# Directly Using Conditions
# NumPy allows us to directly apply conditions on arrays.
arr = np.array([41, 42, 43, 44])
# Directly create a filter
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)  # Output: [False False  True  True]
print(newarr)  # Output: [43 44]
# zip() in a Loop
students = ["John", "Emma", "Liam"]
marks = [90, 85, 88]
for name, mark in zip(students, marks):
    print(f"{name} scored {mark}")

# Broadcasting in NumPy is a way of performing operations on 
# arrays of different sizes without needing to manually change their shapes.
#when performing operations like addition, subtraction, multiplication, or division, 
#both arrays should have the same shape (size and dimensions). However, with broadcasting,
#NumPy automatically expands the smaller array so that it matches the shape of the larger array.
# Adding  the two elements
arr = np.array([1, 2, 3, 4])  # A 1D array
number = 5  # A single number
result = arr + number  # NumPy automatically adds 5 to each element
print(result)
# Adding two arrays of different shapes
arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2,3)
arr2 = np.array([10, 20, 30])  # Shape (3,)
result = arr1 + arr2  # Broadcasting happens
print(result)
# Rules
#Rule 1: If the shapes match, perform the operation normally.
# Rule 2: If one array has a smaller dimension (like fewer rows or columns), NumPy expands it.
# Rule 3: If one dimension is 1, it gets stretched to match the larger array.
# Rule 4: If the shapes don’t match in a way that allows stretching, NumPy throws an error.
arr1 = np.array([[1, 2], [3, 4]])  # Shape (2,2)
arr2 = np.array([1, 2, 3])  # Shape (3,)
#arr2 cannot be stretched to fit (2,2), so NumPy throws an error.
#print(arr1 + arr2)  # This will cause an error!

# For getting index of minimu and maximum value
#np.argmin(arr), np.argmax(arr) → Index of min & max values
# Rotating the array along 90 degree
arr = np.array([[1, 2], [3, 4]])
print(np.rot90(arr))
# Arithmetic operations
#add() function sums the content of two arrays, and return the results in a new array.
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print("Addition::")
print(newarr)
#subtract() function subtracts the values from one array with the values from another array, 
# and return the results in a new array.
newarr = np.subtract(arr1, arr2)
print("Subtraction::")
print(newarr)
# multiply() function multiplies the values from one array with the values from another array,
#  and return the results in a new array.
newarr = np.multiply(arr1, arr2)
print("Multiplication::")
print(newarr)
# Divide the values in arr1 with the values in arr2:
newarr = np.divide(arr1, arr2)
print("Divede::")
print(newarr)
#Raise the valules in arr1 to the power of values in arr2:
newarr = np.power(arr1, arr2)
print("Power::")
print(newarr)
#Both the mod() and the remainder() functions return the remainder of the values in the first array
#  corresponding to the values in the second array
newarr = np.mod(arr1, arr2)
print("mode::")
print(newarr)
# Remainder()
newarr = np.remainder(arr1, arr2)
print("Remainder::")
print(newarr)
#divmod() function return both the quotient and the mod. The return value is two arrays, 
# the first array contains the quotient and second array contains the mod
newarr = np.divmod(arr1, arr2)
print(newarr)
#Both the absolute() and the abs() functions do the same absolute operation element-wise
#  but we should use absolute() to avoid confusion with python's inbuilt math.abs()
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print("Absoulte values::")
print(newarr)

#Summations::Addition is done between two arguments whereas summation happens over n elements.
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])# Sum the values in arr1 and the values in arr2
print("Sum of all elements::",newarr)
#Summation over x axis=1
newarr = np.sum([arr1, arr2], axis=1)
print("Sum of all elements along axis=1::",newarr)
print(newarr)
# cummulative sum
#Cummulative sum means partially adding the elements in array.
#E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
#Perfom partial sum with the cumsum() function.
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print("Cumulative of all elements::",newarr)
print(newarr)
#Product To find the product of the elements in an array, use the prod() function.
arr = np.array([1, 2, 3, 4])
print(" Product of array element::")
x = np.prod(arr) 
print(x) #24 because 1*2*3*4 = 24
# Find Product of two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print("Product of two arrays::")
print(x) #40320 because 1*2*3*4*5*6*7*8 = 40320
# roduct along axisi=1
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr) # [24 1680]
# Cummulative product means taking the product partially.
# E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
#Perfom partial sum with the cumprod() function.
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(" Cumulative product is::")
print(newarr)
# Differences::A discrete difference means subtracting two successive elements.
#E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
# To find the discrete difference, use the diff() function.
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print("Differenc is ::")
print(newarr) # [5 10 -20] because 15-10=5, 25-15=10, and 5-25=-20
#can perform this operation repeatedly by giving parameter n.
#Compute discrete difference of the following array twice
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr) # [5 -30] because: 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30

# Finding LCM of two numbers
#The Lowest Common Multiple (LCM) of two numbers is the smallest number
#  that both numbers can divide evenly.
#Example:Let's take 4 and 6:
#Multiples of 4:
# 👉 4, 8, 12, 16, 20, 24, …
# Multiples of 6:
# 👉 6, 12, 18, 24, 30, …
# The smallest common number in both lists is 12.
# So, LCM of 4 and 6 is 12.
num1 = 4
num2 = 6
x = np.lcm(num1, num2)  # Finding LCM
print(f"LCM of {num1} and {num2} is {x}")  # Output: 12
#The Lowest Common Multiple (LCM) of an array means finding the smallest number 
# that all numbers in the array can divide evenly.
#For multiple numbers (an array), we use np.lcm.reduce(arr).
#The .reduce() function applies np.lcm repeatedly to all numbers in the array,
#  reducing it step by step.
arr = np.array([3, 6, 9])  # Create an array
x = np.lcm.reduce(arr)  # Find LCM of all numbers in the array
print(x)  # Output: 18
# Elaboration of above code of array lcm
#Multiples of 3: 3, 6, 9, 12, 15, 18, …
#Multiples of 6: 6, 12, 18, …
#Multiples of 9: 9, 18, 27, …
#Smallest common number: 18

#LCM of Numbers from 1 to 10
arr = np.arange(1, 11)  # Create an array of numbers from 1 to 10
x = np.lcm.reduce(arr)  # Find LCM of all numbers in the array
print(x)  # Output: 2520


#GCD OR HCF of two numbers
#The Greatest Common Divisor (GCD) (also called Highest Common Factor, HCF) 
# is the largest number that can evenly divide two or more numbers.
#Let's take 6 and 9 and find their GCD.
# Factors of each number:
# Factors of 6: 1, 2, 3, 6
# Factors of 9: 1, 3, 9
# The largest common factor is 3.
# So, GCD of 6 and 9 is 3.
num1 = 6
num2 = 9
x = np.gcd(num1, num2)  # Finding GCD
print(f"GCD of {num1} and {num2} is {x}") # Output: 3
# GCD of array
arr = np.array([20, 8, 32, 36, 16])  # Create an array
x = np.gcd.reduce(arr)  # Find GCD of all numbers in the array
print(x)  # Output: 4
