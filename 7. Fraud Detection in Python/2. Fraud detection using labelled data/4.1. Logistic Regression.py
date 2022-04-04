•	Define a LogisticRegression model with class weights that are 1:15 for the fraud cases.
•	Fit the model to the training set, and obtain the model predictions.
•	Print the classification report and confusion matrix.

# Define the Logistic Regression model with weights
model = LogisticRegression(class_weight={0:1,1:15}, random_state=5)

# Get the model results
get_model_results(X_train, y_train, X_test, y_test, model)
