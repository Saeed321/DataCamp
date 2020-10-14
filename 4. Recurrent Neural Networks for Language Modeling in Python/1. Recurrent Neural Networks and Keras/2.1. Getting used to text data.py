# Getting used to text data

# In this exercise, you will play with text data by analyzing quotes from Sheldon Cooper in The Big Bang Theory TV show. 
# This will give you a chance to analyze sentences to obtain insights on what it's like to deal with real-world text data.

# You will use dictionary comprehensions to create dictionaries that map words to indexes and vice versa. 
# The use of dictionaries instead of, for example, a pandas.DataFrame is because they are more intuitive and don't add unnecessary extra complexity.

# The data is available in sheldon_quotes with the first two sentences already printed for you.
# •	join the sentences into one variable and then extract all the words and store this list in all_words.
# •	Remove the duplicated words by applying list(set()) on the list of words and store them in unique_words.
# •	Create a dictionary with indexes as keys and words as values using dictionary comprehensions.
# •	Create a dictionary with words as keys and indexes as values using dictionary comprehensions.

# Transform the list of sentences into a list of words
all_words = ' '.join(sheldon_quotes).split(' ')

# Get number of unique words
unique_words = list(set(all_words))

# Dictionary of indexes as keys and words as values
index_to_word = {i:wd for i, wd in enumerate(sorted(unique_words))}

print(index_to_word)

# Dictionary of words as keys and indexes as values
word_to_index = {wd:i for i, wd in enumerate(sorted(unique_words))}

print(word_to_index)
