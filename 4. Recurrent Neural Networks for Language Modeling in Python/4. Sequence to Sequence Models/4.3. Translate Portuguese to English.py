# Translate Portuguese to English

# This is the last exercise of the course, congratulations on getting here!
# You will learn how to use NMT models for making translations.
# A model that encodes Portuguese small phrases and decodes them into English small phrases was pre-trained and is loaded in the model variable.
# Also, the function predict_one() is already loaded, use help() for details and the dataset is available on the test (raw text) and X_test(tokenized) variables.
# You will define a function to translate a list of sentences. 
# In the parameters, sentences is a list of phrases to be translated, 
# index_to_word is a dict containing numerical indexes as keys and words as values for the English language, loaded in the en_index_to_word variable.

# The model summary has been printed for your consideration.
# •	Loop over the enumerated iterator of the phrases.
# •	Use the pre-loaded function predict_one() to translate one phrase.
# •	Print the translation result.
# •	Call the defined function to translate the initial 10 phrases of the X_testvariable.

# Function to predict many phrases
def predict_many(model, sentences, index_to_word, raw_dataset):
    for i, sentence in enumerate(sentences):
        # Translate the Portuguese sentence
        translation = predict_one(model, sentence, index_to_word)
        
        # Get the raw Portuguese and English sentences
        raw_target, raw_src = raw_dataset[i]
        
        # Print the correct Portuguese and English sentences and the predicted
        print('src=[%s], target=[%s], predicted=[%s]' % (raw_src, raw_target, translation))

predict_many(model, X_test[0:10], en_index_to_word, test)
