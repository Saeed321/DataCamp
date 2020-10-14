# Prepare label vectors

# In the video exercise, you learned the differences between binary classification and multi-class classification. 
# You learned that there are some modifications to the data preparation process that need to be done before training the models.
# In this exercise, you will prepare a raw dataset with labels given as text. 
# The data is given as a pandas.DataFrame called df, with two columns: textwith the text data and label with the label names. 
# Your task is to make all the necessary transformations to the labels: change string to number and one-hot encode.
# The module pandas as pd and the function to_categorical() from keras.utils.np_utils are already loaded in the environment 
# and the first lines of the dataset is printed on the console for you to see.

# •	Get the attribute .cat.codes of the column label contained on data frame df and print its shape.

# Get the numerical ids of column label
numerical_ids = df.label.cat.codes

# Print initial shape
print(numerical_ids.shape)

# •	One-hot encode the vector using the to_categorical() function and store the results in Y while printing the new shape.

# Get the numerical ids of column label
numerical_ids = df.label.cat.codes

# Print initial shape
print(numerical_ids.shape)

# One-hot encode the indexes
Y = to_categorical(numerical_ids)

# Check the new shape of the variable
print(Y.shape)

# •	Print the first 5 rows of the variable Y.

# Get the numerical ids of column label
numerical_ids = df.label.cat.codes

# Print initial shape
print(numerical_ids.shape)

# One-hot encode the indexes
Y = to_categorical(numerical_ids)

# Check the new shape of the variable
print(Y.shape)

# Print the first 5 rows
print(Y[:5])
