#	Specify all the missing parameters for the mean_target_encoding()function call. Target variable name is "SalePrice". Set α hyperparameter to 10.
#	Recall that the train and test parameters expect the train and test DataFrames.
#	While the target and categorical parameters expect names of the target variable and feature to be encoded.

# Create mean target encoded feature

train['RoofStyle_enc'], test['RoofStyle_enc'] = mean_target_encoding(train=train,
                                                                     test=test,
                                                                     target='SalePrice',
                                                                     categorical='RoofStyle',
                                                                     alpha=10)

# Look at the encoding
print(test[['RoofStyle', 'RoofStyle_enc']].drop_duplicates())
