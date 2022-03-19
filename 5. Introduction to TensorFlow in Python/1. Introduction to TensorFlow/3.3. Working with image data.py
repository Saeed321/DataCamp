•	The model, model, is 1x3 tensor, but should be a 3x1. Reshape model.
•	Perform a matrix multiplication of the 3x3 tensor, letter, by the 3x1 tensor, model.
•	Sum over the resulting tensor, output, and assign this value to prediction.
•	Print prediction using the .numpy() method to determine whether letter is K.

# Reshape model from a 1x3 to a 3x1 tensor
model = reshape(model, (3, 1))

# Multiply letter by model
output = matmul(letter, model)

# Sum over output and print prediction using the numpy method
prediction = reduce_sum(output)
print(prediction.numpy())
