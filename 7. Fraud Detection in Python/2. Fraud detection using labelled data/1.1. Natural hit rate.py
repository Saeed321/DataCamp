•	Count the total number of observations by taking the length of your labels y.
•	Count the non-fraud cases in our data by using list comprehension on y; remember y is a NumPy array so .value_counts() cannot be used in this case.
•	Calculate the natural accuracy by dividing the non-fraud cases over the total observations.
•	Print the percentage.

# Count the total number of observations from the length of y
total_obs = len(y)

# Count the total number of non-fraudulent observations 
non_fraud = [i for i in y if i == 0]
count_non_fraud = non_fraud.count(0)

# Calculate the percentage of non fraud observations in the dataset
percentage = (float(count_non_fraud)/float(total_obs)) * 100

# Print the percentage: this is our "natural accuracy" by doing nothing
print(percentage)
