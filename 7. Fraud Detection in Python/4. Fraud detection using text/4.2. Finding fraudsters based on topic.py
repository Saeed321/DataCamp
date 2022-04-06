•	Print and inspect the results from the get_topic_details() function by inserting your LDA model results and corpus.

# Run get_topic_details function and check the results
print(get_topic_details(ldamodel, corpus))

•	Concatenate column-wise the results from the previously defined function get_topic_details() to the original text data contained under contents and inspect the results.

# Add original text to topic details in a dataframe
contents = pd.DataFrame({'Original text': text_clean})
topic_details = pd.concat([get_topic_details(ldamodel, corpus), contents], axis=1)
print(topic_details.head())

•	Create a flag with the np.where() function to flag all content that has topic 3 as a dominant topic with a 1, and 0 otherwise
# Add original text to topic details in a dataframe
contents = pd.DataFrame({'Original text':text_clean})
topic_details = pd.concat([get_topic_details(ldamodel, corpus), contents], axis=1)

# Create flag for text highest associated with topic 3
topic_details['flag'] = np.where((topic_details['Dominant_Topic'] == 3.0), 1, 0)
print(topic_details.head())
