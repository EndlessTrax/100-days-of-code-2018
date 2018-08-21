'''
1. Create a 3 x 3 NumPy array named first_matrix that includes the numbers 3 through 11 by using arange() and reshape()
2. Display the minimum, maximum and mean of all entries in first_matrix
3. Square every entry in first_matrix using the ** operator, and save the results in an array named second_matrix
4. Use vstack() to stack first_matrix on top of second_matrix and save the results in an array named third_matrix
5. Use dot() to calculate the dot product of third_matrix by first_matrix
6. Reshape third_matrix into an array of dimensions 3 x 3 x 2
'''

from numpy import arange, reshape, dot, vstack 


# Exercise 1
print()
print("Exercse 1")
print("=========\n")

first_matrix = arange(3, 12)
first_matrix = first_matrix.reshape(3,3)

print(first_matrix)

# Exercise 2
print()
print("Exercse 2")
print("=========\n")

print(first_matrix.min())
print(first_matrix.max())
print(first_matrix.mean())

# Exercise 3
print()
print("Exercse 3")
print("=========\n")

second_matrix = first_matrix**2
print(second_matrix)

# Exercise 4
print()
print("Exercse 4")
print("=========\n")

third_matrix = vstack([first_matrix, second_matrix])
print(third_matrix)

# Exercise 5
print()
print("Exercse 5")
print("=========\n")

print(dot(third_matrix, first_matrix))

# Exercise 6
print()
print("Exercse 6")
print("=========\n")

print(third_matrix.reshape(3,3,2))
