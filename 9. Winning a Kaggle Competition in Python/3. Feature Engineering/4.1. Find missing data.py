#	Read the "twosigma_train.csv" file using pandas.
#	Find the number of missing values in each column.

# Read dataframe
twosigma = pd.read_csv('twosigma_train.csv')

# Find the number of missing values in each column
print(twosigma.isnull().sum())

#	Select the columns with the missing values and look at the head of the DataFrame.

# Read DataFrame
twosigma = pd.read_csv('twosigma_train.csv')

# Find the number of missing values in each column
print(twosigma.isnull().sum())

# Look at the columns with the missing values
print(twosigma[["building_id", "price"]].head())
