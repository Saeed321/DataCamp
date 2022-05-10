#	Suggestion 1: the passenger_count feature is useless. Let's see! Drop this feature and compare the scores.

# Drop passenger_count column
new_train_1 = train.drop('passenger_count', axis=1)

# Compare validation scores
initial_score = get_cv_score(train)
new_score = get_cv_score(new_train_1)

print('Initial score is {} and the new score is {}'.format(initial_score, new_score))

#	This first suggestion worked. Suggestion 2: Sum of pickup_latitudeand distance_km is a good feature. Let's try it!

# Create copy of the initial train DataFrame
new_train_2 = train.copy()

# Find sum of pickup latitude and ride distance
new_train_2['weird_feature'] = new_train_2['pickup_latitude'] + new_train_2['distance_km']

# Compare validation scores
initial_score = get_cv_score(train)
new_score = get_cv_score(new_train_2)

print('Initial score is {} and the new score is {}'.format(initial_score, new_score))
