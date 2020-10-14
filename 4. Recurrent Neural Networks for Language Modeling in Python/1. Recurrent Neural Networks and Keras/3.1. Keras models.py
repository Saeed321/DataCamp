# Keras models

# In this exercise you'll practice using two classes from the keras.modelsmodule. 
# You will create one model using the two classes Sequential and Model.

# The Sequential class is easier since the layers are assumed to be in order, 
# while the Model class is more flexible and allows multiple inputs, multiple outputs and shared layers (shared weights).

# The Model class needs to explicitly declare the input layer, while in the Sequential class, this is done with the input_shape parameter.
# The objects and modules Sequential, Model, Dense, Input, LSTMand np (numpy) are already loaded on the environment.
# o	Instantiate theSequential model with name sequential_model.
# o	Add a LSTM and a Dense layers, and print the summary.

# Instantiate the class
model = Sequential(name="sequential_model")

# One LSTM layer (defining the input shape because it is the 
# initial layer)
model.add(LSTM(128, input_shape=(None, 10), name="LSTM"))

# Add a dense layer with one unit
model.add(Dense(1, activation="sigmoid", name="output"))

# The summary shows the layers and the number of parameters 
# that will be trained
model.summary()

# •	Create an Input layer, add LSTM and Dense layers and store in main_output.
# •	Instantiate the model and print its summary.

# Define the input layer
main_input = Input(shape=(None, 10), name="input")

# One LSTM layer (input shape is already defined)
lstm_layer = LSTM(128, name="LSTM")(main_input)

# Add a dense layer with one unit
main_output = Dense(1, activation="sigmoid", name="output")(lstm_layer)

# Instantiate the class at the end
model = Model(inputs=main_input, outputs=main_output, name="modelclass_model")

# Same amount of parameters to train as before (71,297)
model.summary()


