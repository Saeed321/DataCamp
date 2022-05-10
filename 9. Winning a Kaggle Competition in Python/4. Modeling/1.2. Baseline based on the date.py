#	Get the hour from the "pickup_datetime" column for the train and test DataFrames.
#	Calculate the mean "fare_amount" for each hour on the train data.
#	Make test predictions using pandas' map() method and the grouping obtained.
#	Write predictions to the file.


# Get pickup hour from the pickup_datetime column
train['hour'] = train['pickup_datetime'].dt.hour
test['hour'] = test['pickup_datetime'].dt.hour

# Calculate average fare_amount grouped by pickup hour 
hour_groups = train.groupby('hour')['fare_amount'].mean()

# Make predictions on the test set
test['fare_amount'] = test.hour.map(hour_groups)

# Write predictions
test[['id','fare_amount']].to_csv('hour_mean_sub.csv', index=False)
