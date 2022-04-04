•	Define in the parameter grid that you want to try 1 and 30 trees, and that you want to try the gini and entropy split criterion.
•	Define the model to be simple RandomForestClassifier, you want to keep the random_state at 5 to be able to compare models.
•	Set the scoring option such that it optimizes for recall.
•	Fit the model to the training data X_train and y_train and obtain the best parameters for the model.

# Define the parameter sets to test
param_grid = {'n_estimators': [1, 30], 'max_features': ['auto', 'log2'],  'max_depth': [4, 8], 'criterion': ['gini', 'entropy']
}

# Define the model to use
model = RandomForestClassifier(random_state=5)

# Combine the parameter sets with the defined model
CV_model = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='recall', n_jobs=-1)

# Fit the model to our training data and obtain best parameters
CV_model.fit(X_train, y_train)
CV_model.best_params_
