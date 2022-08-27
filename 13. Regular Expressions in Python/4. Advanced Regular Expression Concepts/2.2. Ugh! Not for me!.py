
#	Complete the regular expression to capture the words hate or dislikeor disapprove. Match but don't capture the words movie or concert. Match and capture anything appearing until the ..
#	Find all matches of the regex in each element of sentiment_analysis. Assign them to negative_matches.
#	Complete the .format() method to print out the results contained in negative_matches for each element in sentiment_analysis.

Hint

#	To capture optional groups, use | inside the parentheses. To capture any character use the . metacharacter. Consider using a non-greedy quantifier. To match but not capture a group, use non-capturing syntax ?:. Remember to escape the dot.
#	To find all matches, use .findall().
#	Remember the .format() syntax: "text {}".format(variable).

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)
    
    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))
