•	Find the shapes of the train and test data.
•	Look at the head of the train data.

# Shapes of train and test data
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Train head()
print(train.head())

•	Describe the "fare_amount" column to get some statistics about the target variable.
•	Find the distribution of the "passenger_count" in the train data (using the value_counts() method).

# Shapes of train and test data
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Train head()
print(train.head())

# Describe the target variable
print(train.fare_amount.describe())

# Train distribution of passengers within rides
print(train.passenger_count.value_counts())
