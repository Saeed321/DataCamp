# Exploring 20 News Groups dataset

# In this exercise, you will be given a sample of the 20 News Groups dataset obtained using the fetch_20newsgroups() function from sklearn.datasets, 
# filtering only three classes: sci.space, alt.atheism and soc.religion.christian.

# The dataset is loaded in the variable news_dataset. Its attributes are printed so you can explore them on the console.
# Fore more details on how to use this function, see the Sklearn documentation.

# You will tokenize the texts and one-hot encode the labels step by step to understand how the transformations happen.
# •	Print the example article with index 5 from news_dataset.data.

# See example article
print(news_dataset.data[5])

# •	Transform the data into a sequence of numerical indexes.
# See example article
print(news_dataset.data[5])

# Transform the text into numerical indexes
news_num_indices = tokenizer.texts_to_sequences(news_dataset.data)

# •	Print the transformed example (index 5) article.
# See example article
print(news_dataset.data[5])

# Transform the text into numerical indexes
news_num_indices = tokenizer.texts_to_sequences(news_dataset.data)

# Print the transformed example article
print(news_num_indices[5])

# •	Transform the labels into one-hot vectors using the function to_categorical() and print the original text label 
# and the transformed one-hot vector at index 5 to see the transformed example.
# See example article
print(news_dataset.data[5])

# Transform the text into numerical indexes
news_num_indices = tokenizer.texts_to_sequences(news_dataset.data)

# Print the transformed example article
print(news_num_indices[5])

# Transform the labels into one-hot encoded vectors
labels_onehot = to_categorical(news_dataset.target)

# Check before and after for the sample article
print("Before: {0}\nAfter: {1}".format(news_dataset.target[5], labels_onehot[5]))

