# Precision-Recall trade-off

# When working with classification tasks, the term Precision-Recall trade-off often appears. Where does it comes from?
# Usually, the class with higher probability (obtained by the .predict_proba() method) is chosen to assign the document to. 
# But, what if the maximum probability is equal to 0.1? Should you consider that document to belong to this class with only 10% probability?

# The answer varies according to problem at hand. It is possible to add a minimum threshold to accept the classification, 
# and by changing the threshold the values of precision and recall move in opposite directions.

# The variables y_true and the model model are loaded. Also, if the probability is lower than the threshold, 
# the document will be assigned to DEFAULT_CLASS (chosen to be class 2).
# •	Use the .predict_proba() method to get the probabilities for each class and store them in the pred_probabilities variable.
# •	Accept the maximum probability only if it is greater than or equal to 0.5and store the results in the y_pred_50 variable.
# •	Use the np.argmax() and np.max() functions to do the same for a threshold equal to 0.8.
# •	Print the trade_off variable with all the metrics.

# Get probabilities for each class
pred_probabilities = model.predict_proba(X_test)

# Thresholds at 0.5 and 0.8
y_pred_50 = [np.argmax(x) if np.max(x) >= 0.5 else DEFAULT_CLASS for x in pred_probabilities]
y_pred_80 = [np.argmax(x) if np.max(x) >= 0.8 else DEFAULT_CLASS for x in pred_probabilities]

trade_off = pd.DataFrame({
    'Precision_50': precision_score(y_true, y_pred_50, average=None), 
    'Precision_80': precision_score(y_true, y_pred_80, average=None), 
    'Recall_50': recall_score(y_true, y_pred_50, average=None), 
    'Recall_80': recall_score(y_true, y_pred_80, average=None)}, 
  index=['Class 1', 'Class 2', 'Class 3'])

print(trade_off)
