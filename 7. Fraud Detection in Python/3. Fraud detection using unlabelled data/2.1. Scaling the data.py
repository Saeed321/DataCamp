•	Import the MinMaxScaler.
•	Transform your dataframe df into a numpy array X by taking only the values of df and make sure you have all float values.
•	Apply the defined scaler onto X to obtain scaled values of X_scaled to force all your features to a 0-1 scale.

# Import the scaler
from sklearn.preprocessing import MinMaxScaler

# Take the float values of df for X
X = df.values.astype(np.float)

# Define the scaler and apply to the data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
