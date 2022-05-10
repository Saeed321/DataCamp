#	Create a SimpleImputer object with "mean" strategy.
#	Impute missing prices with the mean value.

# Import SimpleImputer
from sklearn.impute import SimpleImputer

# Create mean imputer
mean_imputer = SimpleImputer(strategy='mean')

# Price imputation
rental_listings[['price']] = mean_imputer.fit_transform(rental_listings[['price']])

#	Create an imputer with "constant" strategy. Use "MISSING" as fill_value.
#	Impute missing buildings with a constant value.

# Import SimpleImputer
from sklearn.impute import SimpleImputer

# Create constant imputer
constant_imputer = SimpleImputer(strategy='constant', fill_value='MISSING')

# building_id imputation
rental_listings[['building_id']] = constant_imputer.fit_transform(rental_listings[['building_id']])
