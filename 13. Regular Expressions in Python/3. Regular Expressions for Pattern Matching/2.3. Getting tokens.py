
#	Write a regex that matches the described hashtag pattern. Assign it to the regex variable.

Hint

#	To match a letter or a number, use \w. If you want these character to be repeated once or multiple times, you can use +. The hashtag symbol will match itself.

# Write a regex matching the hashtag pattern
regex = r"#\w+"

#	Replace all the matches of the regex with an empty string "". Assign it to no_hashtag variable.

Hint

#	To replace a regex with a new sequence, use .sub(). Remember to specify the regex, the new sequence of characters, and the stringinside the method.

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

#	Split the text in the no_hashtag variable at every match of one or more consecutive whitespace.

Hint

#	To split a text at every pattern match, use .split(). To specify you want to split the text at one or more consecutive whitespace (\s), use the + quantifier.

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))
