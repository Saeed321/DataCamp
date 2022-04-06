•	Check the head of df in the console and look for any emails mentioning 'sell enron stock'.

# Find all cleaned emails that contain 'sell enron stock'
mask = df['clean_content'].str.contains('sell enron stock', na=False)
•	Locate the data in df that meets the condition we created earlier.
# Find all cleaned emails that contain 'sell enron stock'
mask = df['clean_content'].str.contains('sell enron stock', na=False)

# Select the data from df using the mask
print(df.loc[mask])
