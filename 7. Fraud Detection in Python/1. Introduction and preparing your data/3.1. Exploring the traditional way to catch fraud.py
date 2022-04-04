•	Use groupby() to group df on Class and obtain the mean of the features.
•	Create the condition V1 smaller than -3, and V3 smaller than -5 as a condition to flag fraud cases.
•	As a measure of performance, use the crosstab function from pandasto compare our flagged fraud cases to actual fraud cases.

# Run a groupby command on our labels and obtain the mean for each feature
df.groupby('Class').mean()

# Implement a rule for stating which cases are flagged as fraud
df['flag_as_fraud'] = np.where(np.logical_and(df['V1'] < -3, df['V3'] < -5), 1, 0)

# Create a crosstab of flagged fraud cases versus the actual fraud cases
print(pd.crosstab(df.Class, df.flag_as_fraud, rownames=['Actual Fraud'], colnames=['Flagged Fraud']))
