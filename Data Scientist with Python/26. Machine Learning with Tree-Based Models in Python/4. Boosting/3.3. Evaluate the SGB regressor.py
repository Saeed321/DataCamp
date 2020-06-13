# Evaluate the SGB regressor

# You have prepared the ground to determine the test set RMSE of sgbrwhich you shall evaluate in this exercise.
# y_pred and y_test are available in your workspace.

# Instructions

# •	Import mean_squared_error as MSE from sklearn.metrics.
# •	Compute test set MSE and assign the result to mse_test.
# •	Compute test set RMSE and assign the result to rmse_test.

# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE

# Compute test set MSE
mse_test = MSE(y_test, y_pred)

# Compute test set RMSE
rmse_test = MSE(y_test, y_pred)**(1/2)

# Print rmse_test
print('Test set RMSE of sgbr: {:.3f}'.format(rmse_test))