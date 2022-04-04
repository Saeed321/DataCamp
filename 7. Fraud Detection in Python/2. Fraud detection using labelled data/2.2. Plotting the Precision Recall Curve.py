•	Calculate the average precision by running the function on the actual labels y_test and your predicted labels predicted.

# Calculate average precision and the PR curve
average_precision = average_precision_score(y_test, predicted)

•	Run the precision_recall_curve() function on the same arguments y_test and predicted and plot the curve (this last thing has been done for you).

# Calculate average precision and the PR curve
average_precision = average_precision_score(y_test, predicted)

# Obtain precision and recall 
precision, recall, _ = precision_recall_curve(y_test, predicted)

# Plot the recall precision tradeoff
plot_pr_curve(recall, precision, average_precision)

Question
What's the benefit of the performance metric ROC curve (AUROC) versus Precision and Recall?

Possible Answers
	 
The AUROC answers the question: "How well can this classifier be expected to perform in general, at a variety of different baseline probabilities?" but precision and recall don't.
	 
The AUROC answers the question: "How meaningful is a positive result from my classifier given the baseline probabilities of my problem?" but precision and recall don't.
	 
Precision and Recall are not informative when the data is imbalanced.
	 
The AUROC curve allows you to visualize classifier performance and with Precision and Recall you cannot.

Answer : The AUROC answers the question: "How well can this classifier be expected to perform in general, at a variety of different baseline probabilities?" but precision and recall don't.
