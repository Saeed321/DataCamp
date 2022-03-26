•	Create 10 random images with shape (1, 28, 28).
•	Create 6 random filters with shape (1, 3, 3).
•	Convolve the images with the filters.

# Create 10 random images
image = torch.rand(10, 1, 28, 28)

# Create 6 filters
filters = torch.rand(6, 1, 3, 3)

# Convolve the image with the filters
output_feature = F.conv2d(image, filters, stride=1, padding=1)
print(output_feature.shape)
