
#	Import the re module.
#	Write a regex to find all the matches of http links appearing in each tweet in sentiment_analysis. Print out the result.
#	Write a regex to find all the matches of user mentions appearing in each tweet in sentiment_analysis. Print out the result.

Hint

#	To import module, use import module.
#	To match a pattern that starts with sequence and has no whitespace, use sequence and \S+. To find all matches, use the method .findall().
#	To match a pattern that starts with @ symbol and can contain letters and numbers, use @ and \w+. To find all matches, use the method .findall().

# Import re module
import re

for tweet in sentiment_analysis:
  	# Write regex to match http links and print out result
	print(re.findall(r"http\S+", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+", tweet))
