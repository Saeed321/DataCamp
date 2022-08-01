
#	Use your model to generate predictions by applying best_lr.transform() to the test data. Save this as test_results.
#	Call evaluator.evaluate() on test_results to compute the AUC. Print the output.

# Use the model to predict the test set
test_results = best_lr.transform(test)

# Evaluate the predictions
print(evaluator.evaluate(test_results))
