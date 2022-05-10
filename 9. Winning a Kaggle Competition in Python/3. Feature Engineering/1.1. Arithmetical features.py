# Create a new feature representing the total area (basement, 1st and 2nd floors) of the house. The columns "TotalBsmtSF", "FirstFlrSF"and "SecondFlrSF" give the areas of the basement, 1st and 2nd floors, respectively.

# Look at the initial RMSE
print('RMSE before feature engineering:', get_kfold_rmse(train))

# Find the total area of the house
train['TotalArea'] = train["TotalBsmtSF"] + train["FirstFlrSF"] + train["SecondFlrSF"]

# Look at the updated RMSE
print('RMSE with total area:', get_kfold_rmse(train))

# Create a new feature representing the area of the garden. It is a difference between the total area of the property ("LotArea") and the first floor area ("FirstFlrSF").

# Look at the initial RMSE
print('RMSE before feature engineering:', get_kfold_rmse(train))

# Find the total area of the house
train['TotalArea'] = train['TotalBsmtSF'] + train['FirstFlrSF'] + train['SecondFlrSF']
print('RMSE with total area:', get_kfold_rmse(train))

# Find the area of the garden
train['GardenArea'] = train["LotArea"] - train["FirstFlrSF"]
print('RMSE with garden area:', get_kfold_rmse(train))

# Create a new feature representing the total number of bathrooms in the house. It is a sum of full bathrooms ("FullBath") and half bathrooms ("HalfBath").

# Look at the initial RMSE
print('RMSE before feature engineering:', get_kfold_rmse(train))

# Find the total area of the house
train['TotalArea'] = train['TotalBsmtSF'] + train['FirstFlrSF'] + train['SecondFlrSF']
print('RMSE with total area:', get_kfold_rmse(train))

# Find the area of the garden
train['GardenArea'] = train['LotArea'] - train['FirstFlrSF']
print('RMSE with garden area:', get_kfold_rmse(train))

# Find total number of bathrooms
train['TotalBath'] = train["FullBath"] + train["HalfBath"]
print('RMSE with number of bathrooms:', get_kfold_rmse(train))
