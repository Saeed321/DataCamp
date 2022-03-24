•	Set the first dense layer to have 32 nodes, use a sigmoid activation function, and have an input shape of (784,).
•	Use the root mean square propagation optimizer, a categorical crossentropy loss, and the accuracy metric.
•	Set the number of epochs to 10 and use 10% of the dataset for validation.

# Define sequential model
model = keras.Sequential()

# Define the first layer
model.add(keras.layers.Dense(32, activation='sigmoid', input_shape=(784,)))

# Add activation function to classifier
model.add(keras.layers.Dense(4, activation='softmax'))

# Set the optimizer, loss function, and metrics
model.compile(optimizer='RMSprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Add the number of epochs and the validation split
model.fit(sign_language_features, sign_language_labels, epochs=10, validation_split=0.10)
