•	Build a max-pooling operator with size 2.
•	Apply the max-pooling operator in the image (loaded as im).
•	Use a max-pooling operator in functional way in the image.
•	Print the results of both cases.

# Build a pooling operator with size `2`.
max_pooling = torch.nn.MaxPool2d(2)

# Apply the pooling operator
output_feature = max_pooling(im)

# Use pooling operator in the image
output_feature_F = F.max_pool2d(im, 2)

# print the results of both cases
print(output_feature)
print(output_feature_F)
