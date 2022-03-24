•	Define a sequential model named model.
•	Set the output layer to be dense, have 4 nodes, and use a softmaxactivation function.
•	Compile the model with the SGD optimizer and categorical_crossentropy loss.
•	Complete the fitting operation and set the number of epochs to 5.

# Define a sequential model
model = keras.Sequential()

# Define a hidden layer
model.add(keras.layers.Dense(16, activation='relu', input_shape=(784,)))

# Define the output layer
model.add(keras.layers.Dense(4, activation='softmax'))

# Compile the model
model.compile('SGD', loss='categorical_crossentropy')

# Complete the fitting operation
model.fit(sign_language_features, sign_language_labels, epochs=5)
