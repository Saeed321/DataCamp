•	Define an ensemble method where you over weigh the second classifier (clf2) with 4 to 1 to the rest of the classifiers.
•	Fit the model to the training and test set, and obtain the predictions predicted from the ensemble model.
•	Print the performance metrics, this is ready for you to run.

# Define the ensemble model
ensemble_model = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)], voting='soft', weights=[1, 4, 1], flatten_transform=True)

# Get results 
get_model_results(X_train, y_train, X_test, y_test, ensemble_model)
