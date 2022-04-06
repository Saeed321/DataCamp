•	Create a list to search for including 'enron stock', 'sell stock', 'stock bonus', and 'sell enron stock'.
•	Join the string terms in the search conditions.
•	Filter data using the emails that match with the list defined under searchfor.

# Create a list of terms to search for
searchfor = ['enron stock', 'sell stock', 'stock bonus', 'sell enron stock']

# Filter cleaned emails on searchfor list and select from df 
filtered_emails = df.loc[df['clean_content'].str.contains('|'.join(searchfor), na=False)]
print(filtered_emails)
