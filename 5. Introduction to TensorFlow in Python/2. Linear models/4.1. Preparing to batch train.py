•	Define intercept as having an initial value of 10.0 and a data type of 32-bit float.
•	Define the model to return the predicted values using intercept, features, and slope.
•	Define a function called loss_function() that takes intercept, slope, targets, and features as arguments. Do not set default argument values.
•	Define the mean squared error loss function using targets and predictions.

# Define the intercept and slope
intercept = Variable(10.0, float32)
slope = Variable(0.5, float32)

# Define the model
def linear_regression(intercept, slope, features):
	# Define the predicted values
	return intercept + features*slope

# Define the loss function
def loss_function(intercept, slope, targets, features):
	# Define the predicted values
	predictions = linear_regression(intercept, slope, features)
    
 	# Define the MSE loss
	return keras.losses.mse(targets, predictions)
