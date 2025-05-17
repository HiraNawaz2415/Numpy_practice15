import numpy as np
# creating 1d array
print("1D array is::")
arr=np.array([[1,2,3,4,89,54]])
print(arr)
# creating 2d array
print("\n2D array is::")
arr1=np.array([[1,4,5,6],[23,45,63,2]])
print(arr1)
print(type(arr))
# creating 3d array
arr3=np.array([[1,2,3],[4,6,8],[9,0,1]])
print("3D array is::")
print(arr3)
# default setting of number of dimensions
arr2=np.array([1,2,3,4],ndmin=4)
print(arr2)
# checking number of dimensions
#The dimension of an array refers to the number of axes or levels
# of indexing required to access elements in the array.
print(" Dimension in arr2 are::")
print(arr2.ndim)
print(" Dimension in arr3 are::")
print(arr3. ndim)
# check number of elements
print(arr.size)
print(arr1.size)
print(arr3.size)
# chcking data type 
print(arr2.dtype)   # Data type of elements
print(arr3.dtype)
print(arr1.dtype)
# shape of array
print("Number of rows and columns in arr1")
print(arr1.shape)
print(arr.shape)
# special arrays
print(np.zeros((3,3)) )  # 3x3 matrix of zeros
print(np.ones((2,4) ) )   # 2x4 matrix of ones
print(np.full((2, 3), 5))  # 2x3 matrix filled with 5
print(np.eye(8) )          # Identity matrix (4x4)

# np.arrange(start,stop,step)
print(np.arange(1,20,3))
# np.linespace(start,stop, numberpoints)
print(np.linspace(1,4,5))

# reshape the array
arr_reshp=np.arange(1,10)
print(arr_reshp)
print("Dimension begore reshaping",arr_reshp.ndim)
print("After Reshaping")
print(arr_reshp.reshape(3,3))
arr_1=arr_reshp.reshape(3,3)
print("Dimension after reshaping",arr_1.ndim)

# Flattening the array
arr=np.array([[1,2,4],[3,4,5]])
print(arr)
print(arr.reshape(-1))
print(arr.flatten())
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 4, -1)
print(newarr.ndim)

print(newarr)

#Basic Syntax of reshape():
#numpy.reshape(a, newshape, order='C')
#a: The input array that you want to reshape.
#newshape: The shape you want the array to have. This is typically specified as a tuple (e.g., (2, 3)) or a single integer (e.g., 6) if you want to flatten it.
#order: (Optional) A character that specifies the order in which the elements are read from the array.
#'C': Row-major (default) order, which means the array is read left-to-right, row by row.
#'F': Column-major order, which means the array is read top-to-bottom, column by column.

# Indexing array
arr = np.array([10, 20, 30, 40, 50])
print(arr[1])
print(arr[-1])
print(arr[-2])
print(arr[2])
# Slicing (Extracting Parts of an Array)
# arr[start:stop:step] syntax
# for 2D array arr[start_row:end_row, start_column:end_column]
#start: The starting index (inclusive).
# stop: The stopping index (exclusive).
# step: The step size, or how many elements to skip.
print(arr[1:3])
print(arr[:3])# first 3 element
print(arr[::2])# every second element
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr2[0:2, 1:4]) # 0:2 (rows)1:4 (columns)
# Modifying elements
arr[-1]=100
print(arr)

# Accessing maximum elemnet
arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
max_elements = np.max(arr, axis=1)
print("Maximum elements in each row:", max_elements)
max_elements = np.max(arr, axis=0)
print("Maximum elements in each column:", max_elements)
min_elements = np.min(arr, axis=1)
print("Minimum elements in each row:", min_elements)
# can also use np.apply_along_axis()
max_elements = np.apply_along_axis(np.max, 1, arr)
min_elements = np.apply_along_axis(np.min, 1, arr)
print("Maximum elements:", max_elements)
print("Minimum elements:", min_elements)

# Element wise operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Sum of element",a+b)
print(a-b)
print(a*b)
print(np.sin(a))
print(np.cos(a))
print(np.exp(a))
print(np.sqrt(a))

# Linear Algebra
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))   
print(A@B)

# Calculating inverse and deteminant
import numpy as np

# 2x2 matrix
A = np.array([[1, 2], [3, 4]])

# Determinant of A
# 2x2 matrix
A = np.array([[1, 2], [3, 4]])

# Determinant of A
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# If the determinant is non-zero, calculate the inverse
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("Inverse of A:\n", inv_A)
else:
    print("Matrix is singular and does not have an inverse.")



# Taking input 2d array from user
# Step 1: Get the number of rows and columns from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Step 2: Initialize an empty list to hold the rows
array = []

# Step 3: Loop through the rows to take input for each row
for i in range(rows):
    row = input(f"Enter values for row {i + 1} separated by space: ").split()
    # Convert the values from strings to integers
    row = [int(x) for x in row]
    array.append(row)

# Step 4: Convert the list of lists into a NumPy 2D array
arr = np.array(array)
# Step 5: Display the 2D array
print("Your 2D array is:")
print(arr)

# Taking input 1D array
# Step 1: Ask the user to enter values for the 1D array
user_input = input("Enter values for the 1D array separated by spaces: ")

# Step 2: Split the input string into a list of strings
input_list = user_input.split()

# Step 3: Convert the list of strings into a list of integers
array_1d = [int(x) for x in input_list]

# Step 4: Convert the list to a NumPy array (optional)
arr = np.array(array_1d)

# Step 5: Display the resulting 1D array
print("Your 1D array is:")
print(arr)

# astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
arr = np.array([1.1, 2.1, 3.1])
arr1=arr.astype(int)
print(arr1)
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
# iterate on aarya
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

# for 2d array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)
# 3d array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
# The function nditer() is a helping function that can be used from very basic to very advanced iterations.
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
# ndenumerate() as a helper that gives you both the index (position) and the value of each element
# idx → holds the index (position) of the current element.
# x → holds the value at that index.
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
# Joining NumPy Arrays
# use the concatenate() function to do this.
arr1 = np.array([1, 2, 3])  # First array
arr2 = np.array([4, 5, 6])  # Second array
arr = np.concatenate((arr1, arr2))  # Joining both arrays
print(arr)
#Join two 2-D arrays along rows (axis=1):
# Joing along column wise
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)


#stacking means combining arrays in different ways.
# We can stack arrays horizontally, vertically, or by depth (height) using special functions.
# (hstack()) joining arrays side by side (horizontally).
arr1 = np.array([1, 2, 3])  # First array
arr2 = np.array([4, 5, 6])  # Second array
arr = np.hstack((arr1, arr2))  # Stacking side by side
print(arr)
# vstack()  stacking arrays on top of each other (vertically).
arr1 = np.array([1, 2, 3])  # First array
arr2 = np.array([4, 5, 6])  # Second array
arr = np.vstack((arr1, arr2))  # Stacking one on top of another
print(arr)
# dstack() stacking arrays in layers (like pages of a book).
arr1 = np.array([1, 2, 3])  # First array
arr2 = np.array([4, 5, 6])  # Second array
arr = np.dstack((arr1, arr2))  # Stacking along depth
print(arr)
# arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
arr = np.array([True, False, True])
print(np.sort(arr))
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

#  an array for a certain value, and return the indexes that get a match.
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
x = np.where(arr%2 == 0)
print(x)
x = np.where(arr%2 == 1)
print(x)
# The searchsorted() function in NumPy helps us find the correct index
#  where a value should be inserted into a sorted array while keeping it sorted.
#Finding Index from the Right (side='right')
#If a number already exists,
#this method returns the next index where the number can go, starting from the right.
arr = np.array([6, 7, 8, 9])  # A sorted array
x = np.searchsorted(arr, 7, side='right')  # Find position for inserting 7
x = np.searchsorted(arr, [2, 4, 6])  # Find positions for 2, 4, and 6
print(x)

#array_split() function to split an array into smaller parts.
# split array into three parts
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)  # Split into 3 parts
print(newarr)
# What if the array doesn't split evenly?
#If the number of elements is not evenly divisible,
#  NumPy adjusts the last array automatically.
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)  # Split into 4 parts
print(newarr)
# array_split() returns a list of arrays. You can access each part using indexing.
print(newarr[0])  # First split array
print(newarr[1])  # Second split array
print(newarr[2])  # Third split array
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)  # Split into 3 parts
print(newarr)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)  # Split along columns
print(newarr)
#hsplit() → Splits along columns.
# vsplit() → Splits along rows.
# dsplit() → Splits along depth (for 3D arrays).
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)  # Split along columns
print(newarr)
