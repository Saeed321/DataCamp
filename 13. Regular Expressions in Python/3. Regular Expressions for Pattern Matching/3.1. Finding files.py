
#	Write a regex that matches the pattern of the text file names, e.g. aemyfile.txt.
#	Find all matches of the regex in the elements of sentiment_analysis. Print out the result.
#	Replace all matches of the regex with an empty string "". Print out the result.

Hint

#	Use [] to indicate optional characters such as [aeiou]. The dot .metacharacter matches any character. The txt ending can match itself. Use ^ to anchor it to the beginning of the string.
#	Use .findall() to find all matches of a regex. Specify regex and string.
#	Use .sub() to replace all matches of a regex. Specify the regex, newsequence, and string.

# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}.+txt"

for text in sentiment_analysis:
	# Find all matches of the regex
	print(re.findall(regex, text))
    
	# Replace all matches with empty string
	print(re.sub(regex, "", text))
