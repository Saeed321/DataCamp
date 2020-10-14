# Preparing the data for training

# In this exercise, you will continue to prepare the data to train the model. 
# After creating the arrays of sentences and next characters, you need to transform them to numerical values that can be used on the model.

# This step is necessary because the RNN models expect numbers only and not strings. 
# You will create numerical arrays that have zeros or ones in the positions representing the characters present on the sentences. 
# Ones (or True) represent the corresponding character is present, while zeros (or False) represent the absence of the character in that position of the sentence.

# The variables sentences, next_char, n_vocab, chars_window, num_seqs (number of sentences in the training data) 
# are already loaded in the environment, as well as numpy as np.
# •	Instantiate a np.array() with zeros and shape (number of sentences, characters window, vocabulary size).
# •	Use the dictionary char_to_index to set the position of the current char to 1.
# •	Set the current next character to 1.
# •	Print the first position of each array.

# Instantiate the variables with zeros
numerical_sentences = np.zeros((num_seqs, chars_window, n_vocab), dtype=np.bool)
numerical_next_chars = np.zeros((num_seqs, n_vocab), dtype=np.bool)

# Loop for every sentence
for i, sentence in enumerate(sentences):
  # Loop for every character in sentence
  for t, char in enumerate(sentence):
    # Set position of the character to 1
    numerical_sentences[i, t, char_to_index[char]] = 1
    # Set next character to 1
    numerical_next_chars[i, char_to_index[next_chars[i]]] = 1

# Print the first position of each
print(numerical_sentences[0], numerical_next_chars[0], sep="\n")
