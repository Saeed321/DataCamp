•	Instantiate a new Sequential() model.
•	Add a Dense() layer with five neurons and three neurons as input.
•	Add a final dense layer with one neuron and no activation.

# Instantiate a new Sequential model
model = Sequential()

# Add a Dense layer with five neurons and three inputs
model.add(Dense(5, input_shape=(3,), activation="relu"))

# Add a final Dense layer with one neuron and no activation
model.add(Dense(1))

# Summarize your model
model.summary()


Question

Given the model you just built, which answer is correct regarding the number of weights (parameters) in the hidden layer?

Possible Answers
	 
There are 15 parameters, 3 for every neuron in the hidden layer.
	 
There are 20 parameters, 15 from the connection of our input layer to our hidden layer and 5 from the bias weight of each neuron in the hidden layer.
	 
There are 20 parameters, no bias weights were needed in this simple model.

Answer : There are 20 parameters, 15 from the connection of our input layer to our hidden layer and 5 from the bias weight of each neuron in the hidden layer.
