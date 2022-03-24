•	Instantiate a Sequential() model.
•	Add a hidden layer of 64 neurons with as many input neurons as there are sensors and relu activation.
•	Add an output layer with as many neurons as parcels and sigmoidactivation.
•	Compile your model with adam and binary_crossentropy loss.

# Instantiate a Sequential model
model = Sequential()

# Add a hidden layer of 64 neurons and a 20 neuron's input
model.add(Dense(64, input_shape=(20,), activation='relu'))

# Add an output layer of 3 neurons with sigmoid activation
model.add(Dense(3, activation='sigmoid'))

# Compile your model with adam and binary crossentropy loss
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.summary()
