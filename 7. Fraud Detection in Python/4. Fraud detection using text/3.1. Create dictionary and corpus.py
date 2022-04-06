•	Import the gensim package and corpora from gensim separately.
•	Define your dictionary by running the correct function on your clean data text_clean.
•	Define the corpus by running doc2bow on each piece of text in text_clean.
•	Print your results so you can see dictionary and corpus look like.

# Import the packages
import gensim
from gensim import corpora

# Define the dictionary
dictionary = corpora.Dictionary(text_clean)

# Define the corpus 
corpus = [dictionary.doc2bow(text) for text in text_clean]

# Print corpus and dictionary
print(dictionary)
print(corpus)
