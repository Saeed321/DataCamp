# Preparing the input text

# You have seen in the video how to prepare the input and output texts. 
# This exercise aims to show a common practice that is to use the maximum length of the sentences to pad all of them, this way no information will be lost.
# Since the RNN models need the inputs to have the same size, this is a way to pad all sentences and just add zeros to the smaller sentences, 
# without cutting the larger ones.
# Also, you will use words instead of characters to represent the tokens, this is a common approach for NMT models.

# The Portuguese texts are loaded on the pt_sentences variable and a fitted tokenizer on the input_tokenizer variable.
# •	Use the .split() method on each sentence to split by white space and obtain the number of words in the sentence.
# •	Use the .texts_to_sequences() method to transform text into sequence of indexes.
# •	Use the obtained maximum length of sentences to pad them.
# •	Print the first transformed sentence.

# Get maximum length of the sentences
pt_length = max([len(line.split()) for line in pt_sentences])

# Transform text to sequence of numerical indexes
X = input_tokenizer.texts_to_sequences(pt_sentences)

# Pad the sequences
X = pad_sequences(X, maxlen=pt_length, padding='post')

# Print first sentence
print(pt_sentences[0])

# Print transformed sentence
print(X[0])
