•	Define a sequential model in keras named model.
•	Add a first dense layer with 1024 nodes, a relu activation, and an input shape of (784,).
•	Set the learning rate to 0.01.
•	Set the fit() operation to iterate over the full sample 200 times and use 50% of the sample for validation purposes.


# Define sequential model
model = keras.Sequential()

# Define the first layer
model.add(keras.layers.Dense(1024, activation='relu', input_shape=(784,)))

# Add activation function to classifier
model.add(keras.layers.Dense(4, activation='softmax'))

# Finish the model compilation
model.compile(optimizer=keras.optimizers.Adam(lr=0.01), 
              loss='categorical_crossentropy', metrics=['accuracy'])

# Complete the model fit operation
model.fit(sign_language_features, sign_language_labels, epochs=200, validation_split=0.50)
