•	Read the test dataset.
•	Print the column names of the train and test datasets.

import pandas as pd

# Read the test data
test = pd.read_csv('test.csv')

# Print train and test columns
print('Train columns:', train.columns.tolist())
print('Test columns:', test.columns.tolist())

•	Notice that test columns do not have the target "sales" column. Now, read the sample submission file.
•	Look at the head of the submission file to get the output format.

import pandas as pd

# Read the test data
test = pd.read_csv('test.csv')
# Print train and test columns
print('Train columns:', train.columns.tolist())
print('Test columns:', test.columns.tolist())

# Read the sample submission file
sample_submission = pd.read_csv('sample_submission.csv')

# Look at the head() of the sample submission
print(sample_submission.head())
