•	Obtain the shape of the dataframe df to inspect the size of our data and display the first rows to see which features are available.

# Get the dataframe shape
df.shape

# Display the first 5 rows
df.head(5)

•	Group the data by transaction category and take the mean of the data.
# Get the dataframe shape
df.shape

# Display the first 5 rows
df.head()

# Groupby categories and take the mean
print(df.groupby('category').mean())

Question

Based on these results, can you already say something about fraud in our data?

Possible Answers
	 
No, I don't have enough information.
	 
Yes, the majority of fraud is observed in travel, leisure and sports related transactions.

Answer : Yes, the majority of fraud is observed in travel, leisure and sports related transactions.
