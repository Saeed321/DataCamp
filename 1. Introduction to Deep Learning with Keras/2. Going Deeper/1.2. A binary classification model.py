•	Import the Sequential model and Dense layer from Keras.
•	Create a sequential model.
•	Add a 1 neuron output layer with sigmoid activation and a 4 neuron input layer with the input_shape parameter.
•	Compile your model using sgd as an optimizer.

# Import the sequential model and dense layer
from keras.models import Sequential
from keras.layers import Dense

# Create a sequential model
model = Sequential()

# Add a dense layer 
model.add(Dense(1, input_shape=(4,), activation='sigmoid'))

# Compile your model
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Display a summary of your model
model.summary()
