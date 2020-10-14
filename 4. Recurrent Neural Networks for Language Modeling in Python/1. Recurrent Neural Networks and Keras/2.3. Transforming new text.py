# Transforming new text

# In this exercise, you will transform a new text into sequences of numerical indexes on the dictionaries created before.

# This is useful when you already have a trained model and want to apply it on a new dataset. 
# The preprocessing steps done on the training data should also be applied to the new text, so the model can make predictions/classifications.
# Here, you will also use a special token '<UKN/>' to represent words that are not in the vocabulary. 
# Typically, these special tokens are the first indexes of the dictionaries, the position 0.

# The variables word_to_index, index_to_word and vocabulary are already loaded in the environment. 
# Also, the variable with the new text is also loaded as new_text. The new text has been printed for you to have a look.
# •	Loop through the list new_text containing the sentences.
# •	Set to 0 the index in case the word is not found in the dictionary.
# •	Append the sentence with indexes to the variable new_text_split.
# •	Convert the indexes back to text using the dictionary index_to_word.

# Loop through the sentences and get indexes
new_text_split = []
for sentence in new_text:
    sent_split = []
    for wd in sentence.split(' '):
        index = word_to_index.get(wd, 0)
        sent_split.append(index)
    new_text_split.append(sent_split)

# Print the first sentence's indexes
print(new_text_split[0])

# Print the sentence converted using the dictionary
print(' '.join([index_to_word[index] for index in new_text_split[0]]))
