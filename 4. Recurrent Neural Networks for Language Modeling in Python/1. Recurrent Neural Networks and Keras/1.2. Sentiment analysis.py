# Sentiment analysis

# In the video exercise, you were exposed to the various applications of sequence to sequence models. 
# In this exercise you will see how to use a pre-trained model for sentiment analysis.

# The model is pre-loaded in the environment on variable model. 
# Also, the tokenized test set variables X_test and y_test and the pre-processed original text data sentences from IMDb are also available.
# You will learn how to pre-process the text data and how to create and train the model using Keraslater in the course.

# You will use the pre-trained model to obtain predictions of sentiment. 
# The model returns a number between zero and one representing the probability of the sentence to have a positive sentiment. 
# So, you will create a decision rule to set the prediction to positive or negative.
# •	Use the .predict() method to make predictions on the test data.
# •	Make the prediction equal to "positive" if its value is greater than 0.5and "negative" otherwise and store the result in the pred_sentimentvariable.
# •	Create a pd.DataFrame containing the pre-processed text, the prediction obtained in the previous step and their true values contained in the y_testvariable.
# •	Print the first rows using the .head() method.

# Inspect the first sentence on `X_test`
print(X_test[0])

# Get the predicion for all the sentences
pred = model.predict(X_test)

# Transform the predition into positive (> 0.5) or negative (<= 0.5)
pred_sentiment = ["positive" if x> 0.5 else "negative" for x in pred]

# Create a data frame with sentences, predictions and true values
result = pd.DataFrame({'sentence': sentences, 'y_pred': pred_sentiment, 'y_true': y_test})

# Print the first lines of the data frame
print(result.head())
