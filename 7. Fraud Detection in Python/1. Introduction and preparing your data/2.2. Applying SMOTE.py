•	Use the prep_data function on df to create features X and labels y.
•	Define the resampling method as SMOTE of the regular kind, under the variable method.
•	Use .fit_sample() on the original X and y to obtain newly resampled data.
•	Plot the resampled data using the plot_data() function.

from imblearn.over_sampling import SMOTE

# Run the prep_data function
X, y = prep_data(df)

# Define the resampling method
method = SMOTE(kind='regular')

# Create the resampled feature set
X_resampled, y_resampled = method.fit_sample(X, y)

# Plot the resampled data
plot_data(X_resampled, y_resampled)
