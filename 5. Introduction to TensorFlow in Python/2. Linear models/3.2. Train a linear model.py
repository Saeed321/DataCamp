•	Initialize an Adam optimizer as opt with a learning rate of 0.5.
•	Apply the .minimize() method to the optimizer.
•	Pass loss_function() with the appropriate arguments as a lambda function to .minimize().
•	Supply the list of variables that need to be updated to var_list.

# Initialize an adam optimizer
opt = keras.optimizers.Adam(0.5)

for j in range(100):
	# Apply minimize, pass the loss function, and supply the variables
	opt.minimize(lambda: loss_function(intercept, slope), var_list=[intercept, slope])

	# Print every 10th value of the loss
	if j % 10 == 0:
		print(loss_function(intercept, slope).numpy())

# Plot data and regression line
plot_results(intercept, slope)
