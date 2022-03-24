•	Set the optimizer to perform minimization.
•	Add the four trainable variables to var_list in the order in which they appear as arguments to loss_function().
•	Use the model and test_features to predict the values for test_targets.

# Train the model
for j in range(100):
    # Complete the optimizer
	opt.minimize(lambda: loss_function(w1, b1, w2, b2), 
                 var_list=[w1, b1, w2, b2])

# Make predictions with model
model_predictions = model(w1, b1, w2, b2, test_features)

# Construct the confusion matrix
confusion_matrix(test_targets, model_predictions)
