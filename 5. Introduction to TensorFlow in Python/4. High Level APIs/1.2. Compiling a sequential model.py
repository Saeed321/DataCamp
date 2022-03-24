•	In the first dense layer, set the number of nodes to 16, the activation to sigmoid, and the input_shape to (784,).
•	Apply dropout at a rate of 25% to the first layer's output.
•	Set the output layer to be dense, have 4 nodes, and use a softmaxactivation function.
•	Compile the model using an adam optimizer and categorical_crossentropy loss function.

# Define the first dense layer
model.add(keras.layers.Dense(16, activation='sigmoid', input_shape=(784,)))

# Apply dropout to the first layer's output
model.add(keras.layers.Dropout(0.25))

# Define the output layer
model.add(keras.layers.Dense(4, activation='softmax'))

# Compile the model
model.compile('adam', loss='categorical_crossentropy')

# Print a model summary
print(model.summary())
