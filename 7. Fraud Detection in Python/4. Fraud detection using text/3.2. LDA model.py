•	Build the LDA model from gensim models, by inserting the corpus and dictionary.
•	Save the 5 topics by running print topics on the model results, and select the top 5 words.

# Define the LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=5)

# Save the topics and top 5 words
topics = ldamodel.print_topics(num_words=5)

# Print the results
for topic in topics:
    print(topic)
