•	Define a keras sequential model named model.
•	Set the first layer to be Dense() and to have 16 nodes and a reluactivation.
•	Define the second layer to be Dense() and to have 8 nodes and a reluactivation.
•	Set the output layer to have 4 nodes and use a softmax activation function.

# Define a Keras sequential model
model = keras.Sequential()

# Define the first dense layer
model.add(keras.layers.Dense(16, activation='relu', input_shape=(784,)))

# Define the second dense layer
model.add(keras.layers.Dense(8, activation='relu'))

# Define the output layer
model.add(keras.layers.Dense(4, activation='softmax'))

# Print the model architecture
print(model.summary())
