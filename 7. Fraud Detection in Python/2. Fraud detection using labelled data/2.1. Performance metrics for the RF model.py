•	Import the classification report, confusion matrix and ROC score from sklearn.metrics.
•	Get the binary predictions from your trained random forest model.
•	Get the predicted probabilities by running the predict_proba() function.
•	Obtain classification report and confusion matrix by comparing y_testwith predicted.

# Import the packages to get the different performance metrics
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Obtain the predictions from our random forest model 
predicted = model.predict(X_test)

# Predict probabilities
probs = model.predict_proba(X_test)

# Print the ROC curve, classification report and confusion matrix
print(roc_auc_score(y_test, probs[:,1]))
print(confusion_matrix(y_test, predicted))
print(classification_report(y_test, predicted))
