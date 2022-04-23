•	Read the train data using pandas.
•	Create a Random Forest object.
•	Train the Random Forest model on the "store" and "item" features with "sales" as a target.

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Read the train data
train = pd.read_csv('train.csv')

# Create a Random Forest object
rf = RandomForestRegressor()

# Train a model
rf.fit(X=train[['store', 'item']], y=train['sales'])
