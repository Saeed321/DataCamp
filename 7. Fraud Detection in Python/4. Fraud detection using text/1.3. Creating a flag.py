•	Use a numpy where condition to flag '1' where the cleaned email contains words on the searchfor list and 0 otherwise.
•	Join the words on the searchfor list with an "or" indicator.
•	Count the values of the newly created flag variable.

# Create flag variable where the emails match the searchfor terms
df['flag'] = np.where((df['clean_content'].str.contains('|'.join(searchfor)) == True), 1, 0)

# Count the values of the flag variable
count = df['flag'].value_counts()
print(count)
