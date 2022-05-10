#	Concatenate the train and test DataFrames into a single DataFrame taxi.
#	Convert the "pickup_datetime" column to a datetime object.
#	Create the day of week (using .dayofweek attribute) and hour (using .hour attribute) features from the "pickup_datetime" column.

# Concatenate train and test together
taxi = pd.concat([train, test])

# Convert pickup date to datetime object
taxi['pickup_datetime'] = pd.to_datetime(taxi['pickup_datetime'])

# Create a day of week feature
taxi['dayofweek'] = taxi['pickup_datetime'].dt.dayofweek

# Create an hour feature
taxi['hour'] = taxi['pickup_datetime'].dt.hour

# Split back into train and test
new_train = taxi[taxi['id'].isin(train['id'])]
new_test = taxi[taxi['id'].isin(test['id'])]
