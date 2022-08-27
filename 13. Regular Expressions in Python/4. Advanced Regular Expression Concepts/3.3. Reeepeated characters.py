
#	Complete the regular expression to match an elongated word as described.
#	Search the elements in sentiment_analysis list to find out if they contain elongated words. Assign the result to match_elongated.
#	Assign the captured group number zero to the variable elongated_word.
#	Print the result contained in the variable elongated_word.

Hint

#	First match the starting characters \w zero or more times. To capture word characters, use (\w+). Reference back to the captured group number m by using \m. Match the ending characters \w zero or more times.
#	To search for a match, use .search().
#	To retrieve the group m, use .group(m).
#	Remember the .format() syntax: "text {variable}".format(variable=string)

# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
	# Find if there is a match in each tweet 
	match_elongated = re.search(regex_elongated, tweet)
    
	if match_elongated:
		# Assign the captured group zero 
		elongated_word = match_elongated.group(0)
        
		# Complete the format method to print the word
		print("Elongated word found: {word}".format(word=elongated_word))
	else:
		print("No elongated word found")     	
