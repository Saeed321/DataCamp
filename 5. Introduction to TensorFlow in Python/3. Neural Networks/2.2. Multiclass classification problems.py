•	Define the input layer as a 32-bit constant tensor using borrower_features.
•	Set the first dense layer to have 10 output nodes and a sigmoid activation function.
•	Set the second dense layer to have 8 output nodes and a rectified linear unit activation function.
•	Set the output layer to have 6 output nodes and the appropriate activation function.

# Construct input layer from borrower features
inputs = constant(borrower_features, float32)

# Define first dense layer
dense1 = keras.layers.Dense(10, activation='sigmoid')(inputs)

# Define second dense layer
dense2 = keras.layers.Dense(8, activation='relu')(dense1)

# Define output layer
outputs = keras.layers.Dense(6, activation='softmax')(dense2)

# Print first five predictions
print(outputs.numpy()[:5])
