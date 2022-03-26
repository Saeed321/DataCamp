•	Build an average-pooling operator with size 2.
•	Apply the average-pooling operator in the image.
•	Use an average-pooling operator in functional way in the image, called im.
•	Print the results of both cases.

# Build a pooling operator with size `2`.
avg_pooling = torch.nn.AvgPool2d(2)

# Apply the pooling operator
output_feature = avg_pooling(im)

# Use pooling operator in the image
output_feature_F = F.avg_pool2d(im, 2)

# print the results of both cases
print(output_feature)
print(output_feature_F)
