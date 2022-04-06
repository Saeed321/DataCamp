•	Obtain the area under the ROC curve from your test labels and predicted labels.
# Obtain the ROC score
print(roc_auc_score(y_test, km_y_pred))

•	Obtain the confusion matrix from the test labels and predicted labels and plot the results.
# Obtain the ROC score
print(roc_auc_score(y_test, km_y_pred))

# Create a confusion matrix
km_cm = confusion_matrix(y_test, km_y_pred)

# Plot the confusion matrix in a figure to visualize results 
plot_confusion_matrix(km_cm)

# Obtain the ROC score
print(roc_auc_score(y_test, km_y_pred))

# Create a confusion matrix
km_cm = confusion_matrix(y_test, km_y_pred)

# Plot the confusion matrix in a figure to visualize results 
plot_confusion_matrix(km_cm)

Question

If you were to decrease the percentile used as a cutoff point in the previous exercise to 93% instead of 95%, what would that do to your prediction results?

Possible Answers
	 
The number of fraud cases caught increases, but false positives also increase.

The number of fraud cases caught decreases, and false positives decrease.

The number of fraud cases caught increases, but false positives would decrease.

Nothing would happen to the amount of fraud cases caught.

Answer : The number of fraud cases caught increases, but false positives also increase.
