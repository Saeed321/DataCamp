•	Define the plot_data(X, y) function, that will nicely plot the given feature set X with labels y in a scatter plot. This has been done for you.
•	Use the function prep_data() on your dataset df to create feature set X and labels y.
•	Run the function plot_data() on your newly obtained X and y to visualize your results.

# Define a function to create a scatter plot of our data and labels
def plot_data(X, y):
	plt.scatter(X[y == 0, 0], X[y == 0, 1], label="Class #0", alpha=0.5, linewidth=0.15)
	plt.scatter(X[y == 1, 0], X[y == 1, 1], label="Class #1", alpha=0.5, linewidth=0.15, c='r')
	plt.legend()
	return plt.show()

# Create X and y from the prep_data function 
X, y = prep_data(df)

# Plot our data by running our plot data function on X and y
plot_data(X, y)
