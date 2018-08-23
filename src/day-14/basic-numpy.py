# Learning Numpy from Real Python Course
from numpy import *


# An  numpy array is like a list but can only have one type of data. i.e. all ints
matrix = array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix)

# You can turn a list into an array
list =[[1,2],[3,4]]
matrix = array(list)

# You can perform calcs on the whole array
matrix = array([[1,2,3], [4,5,6], [7,8,9]])
second_matrix = array([[5,4,3], [7,6,5], [9,8,7]])

print(matrix * 2)
print(second_matrix - matrix)
print(second_matrix * matrix)

# Dot product
print(dot(second_matrix, matrix))

# stacking matrix - note: both take a list as a single arg.
print(vstack([matrix, second_matrix])) # add second_matrix below matrix

print(hstack([matrix, second_matrix])) # add second_matrix next to matrix

# Other common algebra methods
print(matrix.shape) # a tuple of the axis lengths (3 x 3)
print(matrix.diagonal()) # array of the main diagonal entries
print(matrix.flatten()) # a flat array of all entries
print(matrix.transpose()) # mirror-image along the diagonal
print(matrix.min()) # the minimum entry
print(matrix.max()) # the maximum entry
print(matrix.mean()) # the average value of all entries
print(matrix.sum()) # the total of all entries

# Reshaping Matrix
print(matrix.reshape(9,1))

# arange() is similar to range() but returns an array not list
matrix = arange(1,10) # an array of numbers 1 through 9
print(matrix)

matrix = matrix.reshape(3,3)
print(matrix)

# 3 dimensional arrays
array_3d = array([[[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]]])
print(array_3d)

# A better way to create that array would be with reshape() and arange()
array_3d = arange(1,13)
array_3d = array_3d.reshape(3,2,2)
print(array_3d)

# Random is also built into numpy. Can use to randomize array data
print(random.random([3,3]))

