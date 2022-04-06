•	Create a dataframe combining the cluster numbers with the actual labels. This has been done for you.
•	Create a condition that flags fraud for the three smallest clusters: clusters 21, 17 and 9.
•	Create a crosstab from the actual fraud labels with the newly created predicted fraud labels.

# Create a dataframe of the predicted cluster numbers and fraud labels 
df = pd.DataFrame({'clusternr':pred_labels,'fraud':labels})

# Create a condition flagging fraud for the smallest clusters 
df['predicted_fraud'] = np.where((df['clusternr']==21)|(df['clusternr']==17)|(df['clusternr']==9),1 , 0)

# Run a crosstab on the results 
print(pd.crosstab(df['fraud'], df['predicted_fraud'], rownames=['Actual Fraud'], colnames=['Flagged Fraud']))
