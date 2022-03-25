•	Create a matrix of ones with shape 3 by 3, and put it on variable tensor_of_ones.
•	Create an identity matrix with shape 3 by 3, and put it on variable identity_tensor.
•	Do a matrix multiplication of tensor_of_ones with identity_tensorand print its value.
•	Do an element-wise multiplication of tensor_of_ones with identity_tensor and print its value.

# Create a matrix of ones with shape 3 by 3
tensor_of_ones = torch.ones(3, 3)

# Create an identity matrix with shape 3 by 3
identity_tensor = torch.eye(3)

# Do a matrix multiplication of tensor_of_ones with identity_tensor
matrices_multiplied = torch.matmul(tensor_of_ones, identity_tensor)
print(matrices_multiplied)

# Do an element-wise multiplication of tensor_of_ones with identity_tensor
element_multiplication = tensor_of_ones * identity_tensor
print(element_multiplication)
