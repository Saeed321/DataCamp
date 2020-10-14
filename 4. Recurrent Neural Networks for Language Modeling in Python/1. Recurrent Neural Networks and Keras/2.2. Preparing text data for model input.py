# Preparing text data for model input

# Previously, you learned how to create dictionaries of indexes to words and vice versa. 
# In this exercise, you will split the text by characters and continue to prepare the data for supervised learning.

# Splitting the texts into characters may seem strange, but it is often done for text generation. 
# Also, the process to prepare the data is the same, the only change is how to split the texts.

# You will create the training data containing a list of fixed-length texts and their labels, which are the corresponding next characters.
# You will continue to use the dataset containing quotes from Sheldon (The Big Bang Theory), available in the sheldon_quotes variable.

# The print_examples() function print the pairs so you can see how the data was transformed. Use help() for details.
# •	Define step equal to 2 and chars_window equal to 10.
# •	Append the next sentence to the variable sentences.
# •	Append the correct position of the text sheldon to the variable next_chars.
# •	Use the print_examples() function to print 10 sentences and next characters.

# Create lists to keep the sentences and the next character
sentences = []   # ~ Training data
next_chars = []  # ~ Training labels

# Define hyperparameters
step = 2          # ~ Step to take when reading the texts in characters
chars_window = 10 # ~ Number of characters to use to predict the next one  

# Loop over the text: length `chars_window` per time with step equal to `step`
for i in range(0, len(sheldon_quotes) - chars_window, step):
    sentences.append(sheldon_quotes[i:i + chars_window])
    next_chars.append(sheldon_quotes[i + chars_window])

# Print 10 pairs
print_examples(sentences, next_chars, 10)
