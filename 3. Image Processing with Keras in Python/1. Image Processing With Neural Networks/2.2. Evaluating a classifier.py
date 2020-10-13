# Evaluating a classifier

# To evaluate a classifier, we need to test it on images that were not used during training. 
# This is called "cross-validation": a prediction of the class (e.g., t-shirt, dress or shoe) is made from each of the test images, 
# and these predictions are compared with the true labels of these images.

# The results of cross-validation are provided as one-hot encoded arrays: test_labels and predictions.
# �	Multiply the arrays with each other and sum the result to find the total number of correct predictions.
# �	Divide the number of correct answers (the sum) by the length of predictions array to calculate the proportion of correct predictions.

# Calculate the number of correct predictions
number_correct = (test_labels * predictions).sum()
print(number_correct)

# Calculate the proportion of correct predictions
proportion_correct = number_correct / len(predictions)
print(proportion_correct)
