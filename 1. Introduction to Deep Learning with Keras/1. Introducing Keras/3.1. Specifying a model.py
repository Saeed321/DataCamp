•	Instantiate a Sequential model.
•	Add a Dense layer of 50 neurons with an input shape of 1 neuron.
•	Add two Dense layers of 50 neurons each and 'relu' activation.
•	End your model with a Dense layer with a single neuron and no activation.

# Instantiate a Sequential model
model = Sequential()

# Add a Dense layer with 50 neurons and an input of 1 neuron
model.add(Dense(50, input_shape=(1,), activation='relu'))

# Add two Dense layers with 50 neurons and relu activation
model.add(Dense(50,activation='relu'))
model.add(Dense(50,activation='relu'))

# End your model with a Dense layer and no activation
model.add(Dense(1))
