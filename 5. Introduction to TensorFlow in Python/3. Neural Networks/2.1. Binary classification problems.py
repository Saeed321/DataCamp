•	Define inputs as a 32-bit floating point constant tensor using bill_amounts.
•	Set dense1 to be a dense layer with 3 output nodes and a reluactivation function.
•	Set dense2 to be a dense layer with 2 output nodes and a reluactivation function.
•	Set the output layer to be a dense layer with a single output node and a sigmoid activation function.

# Construct input layer from features
inputs = constant(bill_amounts, float32)

# Define first dense layer
dense1 = keras.layers.Dense(3, activation='relu')(inputs)

# Define second dense layer
dense2 = keras.layers.Dense(2, activation='relu')(dense1)

# Define output layer
outputs = keras.layers.Dense(1, activation='sigmoid')(dense2)

# Print error for first five examples
error = default[:5] - outputs.numpy()[:5]
print(error)
