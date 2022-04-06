•	Create two new dataframes from fraud and non-fraud observations. Locate the data in df with .loc and assign the condition "where fraud is 1" and "where fraud is 0" for creation of the new dataframes.
•	Plot the amount column of the newly created dataframes in the histogram plot functions and assign the labels fraud and nonfraud respectively to the plots.

# Create two dataframes with fraud and non-fraud data 
df_fraud = df.loc[df.fraud == 1] 
df_non_fraud = df.loc[df.fraud == 0]

# Plot histograms of the amounts in fraud and non-fraud data 
plt.hist(df_fraud.amount, alpha=0.5, label='fraud')
plt.hist(df_non_fraud.amount, alpha=0.5, label='nonfraud')
plt.legend()
plt.show()
