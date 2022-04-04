•	Set the class_weight argument of your classifier to balanced_subsample.
•	Fit your model to your training set.
•	Obtain predictions and probabilities from X_test.
•	Obtain the roc_auc_score, the classification report and confusion matrix.

# Define the model with balanced subsample
model = RandomForestClassifier(class_weight='balanced_subsample', random_state=5)

# Fit your training model to your training set
model.fit(X_train, y_train)

# Obtain the predicted values and probabilities from the model 
predicted = model.predict(X_test)
probs = model.predict_proba(X_test)

# Print the roc_auc_score, the classification report and confusion matrix
print(roc_auc_score(y_test, probs[:,1]))
print(confusion_matrix(y_test, predicted))
print(classification_report(y_test, predicted))
