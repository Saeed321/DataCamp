#	To achieve this, you need to repeat encoding procedure for the "game_id"categorical feature inside each folds split separately. Your goal is to specify all the missing parameters for the mean_target_encoding() function call inside each folds split.
#	Recall that the train and test parameters expect the train and test DataFrames.
#	While the target and categorical parameters expect names of the target variable and categorical feature to be encoded.

# Create 5-fold cross-validation
kf = KFold(n_splits=5, random_state=123, shuffle=True)

# For each folds split
for train_index, test_index in kf.split(bryant_shots):
    cv_train, cv_test = bryant_shots.iloc[train_index], bryant_shots.iloc[test_index]

    # Create mean target encoded feature
    cv_train['game_id_enc'], cv_test['game_id_enc'] = mean_target_encoding(train=cv_train,
                                                                           test=cv_test,
                                                                           target='shot_made_flag',
                                                                           categorical='game_id',
                                                                           alpha=5)
    # Look at the encoding
    print(cv_train[['game_id', 'shot_made_flag', 'game_id_enc']].sample(n=1))
