•	Set dense1 to be a dense layer with 7 output nodes and a sigmoid activation function.
•	Define dense2 to be dense layer with 3 output nodes and a sigmoid activation function.
•	Define predictions to be a dense layer with 1 output node and a sigmoid activation function.
•	Print the shapes of dense1, dense2, and predictions in that order using the .shape method. Why does each of these tensors have 100 rows?

# Define the first dense layer
dense1 = keras.layers.Dense(7, activation='sigmoid')(borrower_features)

# Define a dense layer with 3 output nodes
dense2 = keras.layers.Dense(3, activation='sigmoid')(dense1)

# Define a dense layer with 1 output node
predictions = keras.layers.Dense(1, activation='sigmoid')(dense2)

# Print the shapes of dense1, dense2, and predictions
print('\n shape of dense1: ', dense1.shape)
print('\n shape of dense2: ', dense2.shape)
print('\n shape of predictions: ', predictions.shape)
