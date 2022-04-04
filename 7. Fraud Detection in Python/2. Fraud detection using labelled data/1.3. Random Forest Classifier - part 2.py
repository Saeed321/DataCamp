•	Fit the earlier defined model to our training data and obtain predictions by getting the model predictions on X_test.

# Fit the model to our training set
model.fit(X_train, y_train)

# Obtain predictions from the test data 
predicted = model.predict(X_test)

•	Obtain and print the accuracy score by comparing the actual labels y_test with our predicted labels predicted.

# Fit the model to our training set
model.fit(X_train, y_train)

# Obtain predictions from the test data 
predicted = model.predict(X_test)

# Print the accuracy performance metric
print(accuracy_score(y_test, predicted))


Question

What is a benefit of using Random Forests versus Decision Trees?

Possible Answers
	 
Random Forests always have a higher accuracy than Decision Trees.
	 
Random Forests do not tend to overfit, whereas Decision Trees do.
	 
Random Forests are computationally more efficient than Decision Trees.
	 
You can obtain "feature importance" from Random Forest, which makes it more transparent.

Answer : Random Forests do not tend to overfit, whereas Decision Trees do.
