#	Split the train DataFrame into two equal parts: part_1 and part_2. Use the train_test_split() function with test_sizeequal to 0.5.
#	Train Gradient Boosting and Random Forest models on the part_1data.

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor

# Split train data into two parts
part_1, part_2 = train_test_split(train, test_size=0.5, random_state=123)

# Train a Gradient Boosting model on Part 1
gb = GradientBoostingRegressor().fit(part_1[features], part_1.fare_amount)

# Train a Random Forest model on Part 1
rf = RandomForestRegressor().fit(part_1[features], part_1.fare_amount)

#	Make Gradient Boosting and Random Forest predictions on the part_2 data.
#	Make Gradient Boosting and Random Forest predictions on the testdata.

# Make predictions on the Part 2 data
part_2['gb_pred'] = gb.predict(part_2[features])
part_2['rf_pred'] = rf.predict(part_2[features])

# Make predictions on the test data
test['gb_pred'] = gb.predict(test[features])
test['rf_pred'] = rf.predict(test[features])
