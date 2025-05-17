# Trignometry functions
# NumPy provides the ufuncs sin(), cos() and tan()
# Find sine value of PI/2:
x = np.sin(np.pi/2)
print(x)
#Find sine values for all of the values in arr
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

#Convert Degrees Into Radians
#radians values are pi/180 * degree_values.
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
#Radians to Degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

#inding angles from values of sine, cos, tan.
#  E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
#NumPy provides ufuncs arcsin(), arccos() and arctan() 
# that produce radian values for corresponding sin, cos and tan values given.
x = np.arcsin(1.0)
print(x)
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

# Hypotenues
#Finding hypotenues using pythagoras theorem in NumPy.
#NumPy provides the hypot() function that takes the base and perpendicular values 
# and produces hypotenues based on pythagoras theorem.
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)

# as it is for hyperbolic function sinh()... etc.


#Set operations 
#Create Sets in NumPy
#We can use NumPy's unique() method to find unique elements from any array.
#  E.g. create a set array, but remember that the set arrays should only be 1-D arrays.
#Convert following array with repeated elements to a set:
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

#Finding Union
#To find the unique values of two arrays, use the union1d() method.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
#Find intersection of the following two set arrays:
#use the intersect1d() method.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
#set1 = np.array([1, 2, 3, 4])
# Define both arrays before using them
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
# Use np.setdiff1d() to find elements in set1 that are NOT in set2
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)  # Output: [1 2]
#Finding Symmetric Difference
#To find only the values that are NOT present in BOTH sets, use the setxor1d() method
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)
#What is assume_unique=True?
#It tells NumPy that both set1 and set2 do not have duplicate values.
#This makes the function run faster.
#If you're unsure, just skip it, as NumPy will handle duplicates automatically.

#Log at Base 2
#Use the log2() function to perform log at the base 2.
arr = np.arange(1, 10)
print(np.log2(arr))
#Log at Base 10
#Use the log10() function to perform log at the base 10.
arr = np.arange(1, 10)
print(np.log10(arr))
#Natural Log, or Log at Base e
#Use the log() function to perform log at the base e.
arr = np.arange(1, 10)
print(np.log(arr))

# creating your own ufunc A ufunc is a NumPy function that works on arrays element by element.
#You can create your own ufunc using np.frompyfunc().
#To check if a function is a ufunc, use type(your_function) == np.ufunc.
#ufuncs are faster and better than normal functions when working with arrays.
# Step 1: Define a normal function
def myadd(x, y):
    return x + y  # Adds two numbers
# Step 2: Convert it into a NumPy ufunc
myadd = np.frompyfunc(myadd, 2, 1)  # (function_name, number_of_inputs, number_of_outputs)
# Step 3: Use it on NumPy arrays
result = myadd([1, 2, 3], [4, 5, 6])
print(result)  # Output: [5 7 9]


#Log at Any Base
#NumPy does not provide any function to take log at any base, 
# so we can use the frompyfunc() function along with inbuilt function math.log()
#  with two input parameters and one output parameter:
from math import log
import numpy as np
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))

#Rounding Decimals in NumPy
#In NumPy, there are five main ways to round decimal numbers:
#Truncation (trunc() and fix()) – Removes the decimal part.
#Rounding (around()) – Rounds based on the nearest value.
#Floor (floor()) – Rounds down to the nearest whole number.
#Ceil (ceil()) – Rounds up to the nearest whole number.
# truc()
arr = np.trunc([-3.1666, 3.6667])  
print(arr)  # Output: [-3.  3.]
arr = np.fix([-3.1666, 3.6667])  
print(arr)  # Output: [-3.  3.]
arr = np.around(3.1666, 2)  
print(arr)  # Output: 3.17
arr = np.floor([-3.1666, 3.6667])  
print(arr)  # Output: [-4.  3.]
arr = np.ceil([-3.1666, 3.6667])  
print(arr)  # Output: [-3.  4.]
