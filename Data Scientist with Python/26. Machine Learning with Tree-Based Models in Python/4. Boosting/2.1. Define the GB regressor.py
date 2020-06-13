# Define the GB regressor

# You'll now revisit the Bike Sharing Demand dataset that was introduced in the previous chapter. Recall that your task is to predict the bike rental demand using historical weather data from the Capital Bikeshare program in Washington, D.C.. For this purpose, you'll be using a gradient boosting regressor.
# As a first step, you'll start by instantiating a gradient boosting regressor which you will train in the next exercise.

# Instructions

# •	Import GradientBoostingRegressor from sklearn.ensemble.
# •	Instantiate a gradient boosting regressor by setting the parameters:
# o	max_depth to 4
# o	n_estimators to 200

# Import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor

# Instantiate gb
gb = GradientBoostingRegressor(n_estimators=200, max_depth=4, random_state=2)