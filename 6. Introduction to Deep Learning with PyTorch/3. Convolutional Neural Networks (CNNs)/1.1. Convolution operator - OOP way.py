•	Create 10 images with shape (1, 28, 28).
•	Build 6 convolutional filters of size (3, 3) with stride set to 1 and padding set to 1.
•	Apply the filters in the image and print the shape of the feature map.

# Create 10 random images of shape (1, 28, 28)
images = torch.rand(10, 1, 28, 28)

# Build 6 conv. filters
conv_filters = torch.nn.Conv2d(in_channels=1, out_channels=6, kernel_size=3, stride=1, padding=1)

# Convolve the image with the filters
output_feature = conv_filters(images)
print(output_feature.shape)
