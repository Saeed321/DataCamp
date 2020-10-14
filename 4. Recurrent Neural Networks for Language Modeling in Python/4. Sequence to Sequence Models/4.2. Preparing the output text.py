# Preparing the output text

# In this exercise, you will prepare the output texts to be used on the translation model. 
# Apart from transforming the text to sequences of indexes, you also need to one-hot encode each index.

# The English texts are loaded on the en_sentences variable, the fitted tokenizer on the output_tokenizer variable 
# and the English vocabulary size on en_vocab_size.

# Also, a function to perform the first steps of transforming the output language (transformation of texts into sequence of indexes) is already created. 
# The function is loaded on the environment as transform_text_to_sequences() and has two parameters: 
# sentencesthat expect a list of sentences in English and tokenizer that expects a fitted Tokenizer object from the keras.preprocessing.text module.
# numpy is loaded as np.
# •	Pass the en_sentences and output_tokenizer variables to the transform_text_to_sequences() function to initialize the Y variable.
# •	Use the to_categorical() function to one-hot encode the sentences. Use the en_vocab_size variable as number of classes.
# •	Transform the temporary list to numpy array and reshape to have shape equal to (num_sentences, sentences_len, en_vocab_size).
# •	Print the raw text and the transformed one.

# Initialize the variable
Y = transform_text_to_sequences(en_sentences, output_tokenizer)

# Temporary list
ylist = list()
for sequence in Y:
  	# One-hot encode sentence and append to list
    ylist.append(to_categorical(sequence, num_classes=en_vocab_size))

# Update the variable
Y = np.array(ylist).reshape(Y.shape[0], Y.shape[1], en_vocab_size)

# Print the raw sentence and its transformed version
print("Raw sentence: {0}\nTransformed: {1}".format(en_sentences[0], Y[0]))
