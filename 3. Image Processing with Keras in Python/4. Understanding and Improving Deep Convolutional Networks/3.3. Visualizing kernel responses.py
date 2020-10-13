# Visualizing kernel responses

# One of the ways to interpret the weights of a neural network is to see how the kernels stored in these weights "see" the world. 
# That is, what properties of an image are emphasized by this kernel. 
# In this exercise, we will do that by convolving an image with the kernel and visualizing the result. 
# Given images in the test_data variable, a function called extract_kernel() that extracts a kernel from the provided network, 
# and the function called convolution() that we defined in the first chapter, extract the kernel, load the data from a file and visualize it with matplotlib.

# A deep CNN model, a function convolution(), along with the kernelyou extracted in an earlier exercise is available in your workspace.
# �	Use the convolution() function to convolve the extracted kernel with the first channel of the fourth item in the image array.
# �	Visualize the resulting convolution with imshow().

import matplotlib.pyplot as plt

# Convolve with the fourth image in test_data
out = convolution(test_data[3, :, :, 0], kernel)

# Visualize the result
plt.imshow(out)
plt.show()
