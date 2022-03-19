•	Define a function that returns the predicted values for a linear regression using intercept, features, and slope, and without using add()or multiply().
•	Complete the loss_function() by adding the model's variables, intercept and slope, as arguments.
•	Compute the mean squared error using targets and predictions.

# Define a linear regression model
def linear_regression(intercept, slope, features = size_log):
	return (intercept + features*slope)

# Set loss_function() to take the variables as arguments
def loss_function(intercept, slope, features = size_log, targets = price_log):
	# Set the predicted values
	predictions = linear_regression(intercept, slope, features)
    
    # Return the mean squared error loss
	return keras.losses.mse(targets, predictions)

# Compute the loss for different slope and intercept values
print(loss_function(0.1, 0.1).numpy())
print(loss_function(0.1, 0.5).numpy())
