# Word2Vec

# In this exercise you will create a Word2Vec model using Keras.
# The corpus used to pre-train the model is the script of all episodes of the The Big Bang Theory TV show, divided sentence by sentence. 
# It is available in the variable bigbang.

# The text on the corpus was transformed to lower case and all words were tokenized. The result is stored in the tokenized_corpus variable.

# A Word2Vec model was pre-trained using a window size of 10 words for context (5 before and 5 after the center word), 
# words with less than 3 occurrences were removed and the skip gram model method was used with 50 dimension. 
# The model is saved on the file bigbang_word2vec.model.

# The class Word2Vec is already loaded in the environment from gensim.models.word2vec.
# •	Load the pre-trained Word2Vec model.
# •	Store a list with the words "bazinga", "penny", "universe", "spock", "brain" in the variable words_of_interest, keeping them in that order.
# •	Iterate over each word of interest while using the .most_similar()method present on attribute wv and 
# append the top 5 similar words to top5_similar_words as a dictionary.
# •	Print the found top 5 words for each of the words of interest.

# Word2Vec model
w2v_model = Word2Vec.load('bigbang_word2vec.model')

# Selected words to check similarities
words_of_interest = ["bazinga", "penny", "universe", "spock", "brain"]

# Compute top 5 similar words for each of the words of interest
top5_similar_words = []
for word in words_of_interest:
    top5_similar_words.append(
      {word: [item[0] for item in w2v_model.wv.most_similar([word], topn=5)]}
    )

# Print the similar words
print(top5_similar_words)
