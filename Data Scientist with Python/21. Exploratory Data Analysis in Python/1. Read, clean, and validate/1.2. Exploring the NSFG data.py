# Exploring the NSFG data

# To get the number of rows and columns in a DataFrame, you can read its shape attribute.
# To get the column names, you can read the columns attribute. The result is an Index, which is a Pandas data structure that is similar to a list. Let's begin exploring the NSFG data! It has been pre-loaded for you into a DataFrame called nsfg.

# �	Calculate the number of rows and columns in the DataFrame nsfg.

# Display the number of rows and columns
print(nsfg.shape)
print(nsfg.columns)

# �	Display the names of the columns in nsfg.

# Display the number of rows and columns
nsfg.shape

# Display the names of the columns
print(nsfg.columns)
# �	Select the column 'birthwgt_oz1' and assign it to a new variable called ounces.

# Display the number of rows and columns
nsfg.shape

# Display the names of the columns
nsfg.columns

# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']


# �	Display the first 5 elements of ounces.

# Display the number of rows and columns
nsfg.shape

# Display the names of the columns
nsfg.columns

# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

# Print the first 5 elements of ounces
print(ounces.head())