#	Determine the distribution of "RoofStyle" and "CentralAir" features using pandas' value_counts() method.

# Concatenate train and test together
houses = pd.concat([train, test])

# Look at feature distributions
print(houses['RoofStyle'].value_counts(), '\n')
print(houses['CentralAir'].value_counts())


#	Which of the features is binary?

"RoofStyle".
Answer : "CentralAir".

#	As long as "CentralAir" is a binary feature, encode it with a label encoder (0 - for one class and 1 - for another class).

# Concatenate train and test together
houses = pd.concat([train, test])

# Label encode binary 'CentralAir' feature
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
houses['CentralAir_enc'] = le.fit_transform(houses['CentralAir'])

#	For the categorical feature "RoofStyle" let's use the one-hot encoder. Firstly, create one-hot encoded features using the get_dummies()method. Then they are concatenated to the initial houses DataFrame.

# Concatenate train and test together
houses = pd.concat([train, test])

# Label encode binary 'CentralAir' feature
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
houses['CentralAir_enc'] = le.fit_transform(houses['CentralAir'])

# Create One-Hot encoded features
ohe = pd.get_dummies(houses['RoofStyle'], prefix='RoofStyle')

# Concatenate OHE features to houses
houses = pd.concat([houses, ohe], axis=1)

# Look at OHE features
print(houses[[col for col in houses.columns if 'RoofStyle' in col]].head(3))
