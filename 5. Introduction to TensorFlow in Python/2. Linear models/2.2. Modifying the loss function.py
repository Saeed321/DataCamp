•	Define a variable, scalar, with an initial value of 1.0 and a type of float32.
•	Define a function called loss_function(), which takes scalar, features, and targets as arguments in that order.
•	Use a mean absolute error loss function.

# Initialize a variable named scalar
scalar = Variable(1.0, float32)

# Define the model
def model(scalar, features = features):
  	return scalar * features

# Define a loss function
def loss_function(scalar, features = features, targets = targets):
	# Compute the predicted values
	predictions = model(scalar, features)
    
	# Return the mean absolute error loss
	return keras.losses.mae(targets, predictions)

# Evaluate the loss function and print the loss
print(loss_function(scalar).numpy())
