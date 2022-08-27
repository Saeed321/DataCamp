
#	Complete the regex to match the email capturing only the name part. The name part appears before the @.
#	Find all matches of the regex in each element of sentiment_analysisanalysis. Assign it to the variable email_matched.
#	Complete the .format() method to print the results captured in each element of sentiment_analysis analysis.

Hint

#	To capture a group, place parentheses to surround that group: (group)regex. To match any lowercase letter use a-z, any uppercase use A-Z and numbers 0-9. Use [] to indicate optional characters. Use + to match once or more times. @ will match itself.
#	To find all matches of a regex, use .findall().
#	Remember the .format() syntax: "text {}".format(string).

# Write a regex that matches email
regex_email = r"([A-Za-z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))
