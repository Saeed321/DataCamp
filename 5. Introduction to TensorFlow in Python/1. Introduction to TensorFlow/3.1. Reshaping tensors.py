•	Reshape gray_tensor from a 28x28 matrix into a 784x1 vector named gray_vector.
•	Reshape color_tensor from a 28x28x3 tensor into a 2352x1 vector named color_vector.

# Reshape the grayscale image tensor into a vector
gray_vector = reshape(gray_tensor, (784, 1))

# Reshape the color image tensor into a vector
color_vector = reshape(color_tensor, (2352, 1))
