•	Split X and y into training and test data, keeping 30% of the data for testing.
•	Fit your model to your training data.
•	Obtain the model predicted labels by running model.predict on X_test.
•	Obtain a classification comparing y_test with predicted, and use the given confusion matrix to check your results.

# Create the training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Fit a logistic regression model to our data
model = LogisticRegression()
model.fit(X_train, y_train)

# Obtain model predictions
predicted = model.predict(X_test)

# Print the classifcation report and confusion matrix
print('Classification report:\n', classification_report(y_test, predicted))
conf_mat = confusion_matrix(y_true=y_test, y_pred=predicted)
print('Confusion matrix:\n', conf_mat)
