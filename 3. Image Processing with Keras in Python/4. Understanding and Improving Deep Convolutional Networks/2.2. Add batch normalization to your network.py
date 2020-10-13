# Add batch normalization to your network

# Batch normalization is another form of regularization that rescales the outputs of a layer to make sure that they have mean 0 and standard deviation 1. 
# In this exercise, we will add batch normalization to the convolutional neural network that we have used in previous exercises:
# 1.	Convolution (15 units, kernel size 2, 'relu' activation)
# 2.	Batch normalization
# 3.	Convolution (5 unites, kernel size 2, 'relu' activation)
# 4.	Flatten
# 5.	Dense (3 units, 'softmax' activation)

# A Sequential model along with Dense, Conv2D, Flatten, and Dropout objects are available in your workspace.
# •	Add the first convolutional layer. You can use the img_rows and img_cols objects available in your workspace to define the input_shape of this layer.
# •	Add batch normalization applied to the outputs of the first layer.

# Add a convolutional layer
model.add(Conv2D(15, kernel_size=2, activation='relu', 
                 input_shape=(img_rows, img_cols, 1)))

# Add batch normalization layer
model.add(BatchNormalization())

# Add another convolutional layer
model.add(Conv2D(5, kernel_size=2, activation='relu'))

# Flatten and feed to output layer
model.add(Flatten())
model.add(Dense(3, activation='softmax'))
