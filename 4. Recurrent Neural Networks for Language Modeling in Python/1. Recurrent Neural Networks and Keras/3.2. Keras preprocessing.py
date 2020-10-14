# Keras preprocessing

# The second most important module of Keras is keras.preprocessing. 
# You will see how to use the most important modules and functions to prepare raw data to the correct input shape. 
# Keras provides functionalities that substitute the dictionary approach you learned before.

# You will use the module keras.preprocessing.text.
# Tokenizer to create a dictionary of words using the method .fit_on_texts() and 
# change the texts into numerical ids representing the index of each word on the dictionary using the method .texts_to_sequences().

# Then, use the function .pad_sequences() from keras.preprocessing.sequence 
# to make all the sequences have the same size (necessary for the model) by adding zeros on the small texts and cutting the big ones.
# •	Import Tokenizer and pad_sequences from relevant modules.
# •	Fit the tokenizer object on the sample data stored in texts.
# •	Transform the texts into sequences of numerical indexes using the method .texts_to_sequences().
# •	Fix the size of the texts by padding them.

# Import relevant classes/functions
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Build the dictionary of indexes
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

# Change texts into sequence of indexes
texts_numeric = tokenizer.texts_to_sequences(texts)
print("Number of words in the sample texts: ({0}, {1})".format(len(texts_numeric[0]), len(texts_numeric[1])))

# Pad the sequences
texts_pad = pad_sequences(texts_numeric, 60)
print("Now the texts have fixed length: 60. Let's see the first one: \n{0}".format(texts_pad[0]))


