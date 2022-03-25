•	Import PyTorch main library.
•	Create the variable your_first_tensor and set it to a random torch tensor of size 3 by 3.
•	Calculate its shape (dimension sizes) and set it to variable tensor_size.
•	Print the values of your_first_tensor and tensor_size.

# Import torch
import torch

# Create random tensor of size 3 by 3
your_first_tensor = torch.rand(3, 3)

# Calculate the shape of the tensor
tensor_size = your_first_tensor.shape

# Print the values of the tensor and its shape
print(your_first_tensor)
print(tensor_size)
