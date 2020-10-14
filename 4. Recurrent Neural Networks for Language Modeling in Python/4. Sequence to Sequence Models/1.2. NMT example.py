# NMT example

# This exercise aims to build on the sneak peek you got of NMT at the beginning of the course. 
# You will continue to translate Portuguese small phrases into English.
# Some sample sentences are available on the sentences variable and are printed on the console.
# Also, a pre-trained model is available on the model variable and you will use two custom functions to simplify some steps:
# •	encode_sequences(): Change texts into sequence of numerical indexes and pad them.
# •	translate_many(): Uses the pre-trained model to translate a list of sentences from Portuguese into English. Later you will code this function yourself.

# For more details on the functions, use help(). The package pandas is loaded as pd.
# •	Use the encode_sequences() function to pre-process the texts and save the results in the X variable.
# •	Translate the sentences using the translate_many() function by passing X as a parameter.
# •	Create a pd.DataFrame() with the original and translated lists as columns.
# •	Print the data frame.

# Transform text into sequence of indexes and pad
X = encode_sequences(sentences)

# Print the sequences of indexes
print(X)

# Translate the sentences
translated = translate_many(model, X)

# Create pandas DataFrame with original and translated
df = pd.DataFrame({'Original': sentences, 'Translated': translated})

# Print the DataFrame
print(df)