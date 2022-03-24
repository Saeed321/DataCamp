•	Use a deep neural network regressor with 2 nodes in both the first and second hidden layers and 1 training step.

# Define the model and set the number of steps
model = estimator.DNNRegressor(feature_columns=feature_list, hidden_units=[2,2])
model.train(input_fn, steps=1)

•	Modify the code to use a LinearRegressor(), remove the hidden_units, and set the number of steps to 2.

# Define the model and set the number of steps
model = estimator.LinearRegressor(feature_columns=feature_list)
model.train(input_fn, steps=2)
