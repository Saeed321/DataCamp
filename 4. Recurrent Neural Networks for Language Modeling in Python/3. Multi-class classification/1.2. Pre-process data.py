# Pre-process data

# You learned the differences for pre-processing the data in the case of multi-class classification. 
# Let's put that into practice by preprocessing the data in anticipation of creating a simple multi-class classification model.

# The dataset is loaded in the variable news_dataset, and has the following attributes:
# •	news_dataset.data: array with texts
# •	news_dataset.target: array with target categories as numerical indexes
# •	news_dataset.target_names: array with the unique names as strings of the target categories

# The sample data contains 5,000 observations.
# •	Instantiate the Tokenizer class on the tokenizer variable.
# •	Fit the tokenizer variable on the text data.
# •	Use the .texts_to_sequences() method on the text data.
# •	Use the to_categorical() function to prepare the target indexes.

# Create and fit tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(news_dataset)

# Prepare the data
prep_data = tokenizer.texts_to_sequences(news_dataset.data)
prep_data = pad_sequences(prep_data, maxlen=200)

# Prepare the labels
prep_labels = to_categorical(news_dataset.target)

# Print the shapes
print(prep_data.shape)
print(prep_labels.shape)
