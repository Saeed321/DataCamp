•	Import the Pipeline module from imblearn, this has been done for you.
•	Then define what you want to put into the pipeline, assign the SMOTEmethod with borderline2 to resampling, and assign LogisticRegression() to the model.
•	Combine two steps in the Pipeline() function. You need to state you want to combine resampling with the model in the respective place in the argument. I show you how to do this.

# This is the pipeline module we need for this from imblearn
from imblearn.pipeline import Pipeline 

# Define which resampling method and which ML model to use in the pipeline
resampling = SMOTE(kind='borderline2')
model = LogisticRegression()

# Define the pipeline, tell it to combine SMOTE with the Logistic Regression model
pipeline = Pipeline([('SMOTE', resampling), ('Logistic Regression', model)])
