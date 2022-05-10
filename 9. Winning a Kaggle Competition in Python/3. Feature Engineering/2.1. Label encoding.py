#	Concatenate train and test DataFrames into a single DataFrame houses.
#	Create a LabelEncoder object without arguments and assign it to le.
#	Create new label-encoded features for "RoofStyle" and "CentralAir" using the same le object.

# Concatenate train and test together
houses = pd.concat([train, test])

# Label encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# Create new features
houses['RoofStyle_enc'] = le.fit_transform(houses['RoofStyle'])
houses['CentralAir_enc'] = le.fit_transform(houses['CentralAir'])

# Look at new features
print(houses[['RoofStyle', 'RoofStyle_enc', 'CentralAir', 'CentralAir_enc']].head())
