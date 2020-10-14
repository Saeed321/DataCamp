# Create vectors of sentences and next characters

# This exercise aims to emphasize more the value of data preparation. 
# You will use texts containing phrases of the character Sheldon from The Big Bang Theory TV show as input 
# and will create vectors of sentence indexes and next characters that are needed before creating a text generation model.

# The text is available in the sheldon variable, as well as the vocabulary (characters) on the vocabulary variable 
# and the hyperparameters chars_window and step defined with values 20 and 3. 
# This means that a sequence of 20 characters will be used to predict the next one, and the window will shift 3 characters on every iteration.
# Also, the package pandas as pd is loaded in the environment.
# •	Split the text by line break to loop through sentences.
# •	Loop until the end of the sentence minus chars_window.
# •	Append the portion of the sentence that has chars_window characters to the sentences variable and append the next character to the next_chars variable.
# •	Use the obtained vectors to create a pd.DataFrame() and print its first rows.

# Instantiate the vectors
sentences = []
next_chars = []
# Loop for every sentence
for sentence in sheldon.split('\n'):
    # Get 20 previous chars and next char; then shift by step
    for i in range(0, len(sentence) - chars_window, step):
        sentences.append(sentence[i:i + chars_window])
        next_chars.append(sentence[i + chars_window])

# Define a Data Frame with the vectors
df = pd.DataFrame({'sentence': sentences, 'next_char': next_chars})

# Print the initial rows
print(df.head())