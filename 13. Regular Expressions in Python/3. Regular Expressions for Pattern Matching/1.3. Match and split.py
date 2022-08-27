
#	Write a regex that matches the pattern separating the sentences in sentiment_analysis, e.g. &4break!.

Hint

#	Start a regex with r. Use \W to match special characters and \d to match digits. Don't forget that normal characters match themselves.

# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

#	Replace regex_sentence with a space " " in the variable sentiment_analysis. Assign it to sentiment_sub.

Hint

#	To replace a regex in a string, use the method .sub of the remodule. Don't forget to specify regex, the new characters and the string inside the method.

# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

#	Write a regex that matches the pattern separating the words in sentiment_analysis, e.g. #newH.

Hint

#	Start a regex with r. Use \W to match special characters and \w to match any word character. Don't forget that normal characters match themselves.
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

#	Replace regex_words with a space in the variable sentiment_sub. Assign it to sentiment_final and print out the result.

Hint

#	To replace a regex in a string, use the method .sub of the remodule. Don't forget to specify regex, the new characters and the string inside the method.
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)
