•	Print the value counts of our original labels, y. Be mindful that y is currently a Numpy array, so in order to use value counts, we'll assign y back as a pandas Series object.
•	Repeat the step and print the value counts on y_resampled. This shows you how the balance between the two classes has changed with SMOTE.
•	Use the compare_plot() function called on our original data as well our resampled data to see the scatterplots side by side.

# Print the value_counts on the original labels y
print(pd.value_counts(pd.Series(y)))

# Print the value_counts
print(pd.value_counts(pd.Series(y_resampled)))

# Run compare_plot
compare_plot(X, y, X_resampled, y_resampled, method='SMOTE')
