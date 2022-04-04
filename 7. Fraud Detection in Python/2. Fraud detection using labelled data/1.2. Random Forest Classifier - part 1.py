•	Import the random forest classifier from sklearn.
•	Split your features X and labels y into a training and test set. Set aside a test set of 30%.
•	Assign the random forest classifier to model and keep random_state at 5. We need to set a random state here in order to be able to compare results across different models.

# Import the random forest model from sklearn
from sklearn.ensemble import RandomForestClassifier

# Split your data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Define the model as the random forest
model = RandomForestClassifier(random_state=5)
