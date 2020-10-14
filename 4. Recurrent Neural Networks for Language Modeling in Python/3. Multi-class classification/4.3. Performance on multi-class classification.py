# Performance on multi-class classification

# In this exercise, you will compute the performance metrics for models using the module sklearn.metrics.
# The model is already trained and stored in the variable model. 
# Also, the variables X_test and y_true are also loaded, together with the functions confusion_matrix() 
# and classification_report() from sklearn.metrics package.

# You will first compute the confusion matrix of the model. 
# Then, to summarize a model's performance, you will compute the precision, recall and F1-score using the classification_report() function. 
# In this function, you can optionally pass a list containing the classes names (they are stored it in the news_cat variable) 
# to the parameter target_names to make the report more readable.
# •	Make the predictions on the X_test and store it in predicted.
# •	Get the class predicted with the higher probability using np.argmax(axis=1) and stored it in y_pred.

# Use the model to predict on new data
predicted = model.predict(X_test)

# Choose the class with higher probability 
y_pred = np.argmax(predicted, axis=1)

# •	Compute the confusion matrix using the function confusion_matrix().
# Use the model to predict on new data
predicted = model.predict(X_test)

# Choose the class with higher probability 
y_pred = np.argmax(predicted, axis=1)

# Compute and print the confusion matrix
print(confusion_matrix(y_true, y_pred))

# •	Print the classification_report() to see the formatted report.
# Use the model to predict on new data
predicted = model.predict(X_test)

# Choose the class with higher probability 
y_pred = np.argmax(predicted, axis=1)

# Compute and print the confusion matrix
print(confusion_matrix(y_true, y_pred))

# Create the performance report
print(classification_report(y_true, y_pred, target_names=news_cat))
