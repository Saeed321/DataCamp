•	Read "test.csv" and "sample_submission.csv" files using pandas.
•	Look at the head of the sample submission to determine the format.

# Read test and sample submission data
test = pd.read_csv('test.csv')
sample_submission = pd.read_csv('sample_submission.csv')

# Show the head() of the sample_submission
print(sample_submission.head())

•	Note that sample submission has id and sales columns. Now, make predictions on the test data using the rf model, that you fitted on the train data.
•	Using the format given in the sample submission, write your results to a new file.

# Read test and sample submission data
test = pd.read_csv('test.csv')
sample_submission = pd.read_csv('sample_submission.csv')

# Show the head() of the sample_submission
print(sample_submission.head())

# Get predictions for the test set
test['sales'] = rf.predict(test[['store', 'item']])

# Write test predictions using the sample_submission format
test[['id', 'sales']].to_csv('kaggle_submission.csv', index=False)
