•	Input the optimal settings into the model definition.
•	Fit the model, obtain predictions and get the performance parameters with get_model_results().

# Input the optimal parameters in the model
model = RandomForestClassifier(class_weight={0:1,1:12}, criterion='gini',
            n_estimators=30, max_features='log2',  min_samples_leaf=10, max_depth=8, n_jobs=-1, random_state=5)

# Get results from your model
get_model_results(X_train, y_train, X_test, y_test, model)
