•	Import pandas as pd, read the credit card data in and assign it to df. This has been done for you.
•	Use .info() to print information about df.
•	Use .value_counts() to get the count of fraudulent and non-fraudulent transactions in the'Class' column. Assign the result to occ.
•	Get the ratio of fraudulent transactions over the total number of transactions in the dataset.

# Import pandas and read csv
import pandas as pd
df = pd.read_csv("creditcard_data.csv")

# Explore the features available in your dataframe
print(df.info())

# Count the occurrences of fraud and no fraud and print them
occ = df['Class'].value_counts()
print(occ)

# Print the ratio of fraud cases
print(occ / len(df))
