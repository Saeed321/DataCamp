•	Define the tensors A1 and A23 as constants.
•	Set B1 to be a tensor of ones with the same shape as A1.
•	Set B23 to be a tensor of ones with the same shape as A23.
•	Set C1 and C23 equal to the element-wise products of A1 and B1, and A23 and B23, respectively.


# Define tensors A1 and A23 as constants
A1 = constant([1, 2, 3, 4])
A23 = constant([[1, 2, 3], [1, 6, 4]])

# Define B1 and B23 to have the correct shape
B1 = ones_like(A1)
B23 = ones_like(A23)

# Perform element-wise multiplication
C1 = multiply(A1, B1)
C23 = multiply(A23, B23)

# Print the tensors C1 and C23
print('C1: {}'.format(C1.numpy()))
print('C23: {}'.format(C23.numpy()))
