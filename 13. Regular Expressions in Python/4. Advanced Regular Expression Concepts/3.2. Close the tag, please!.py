
#	Complete the regex in order to match closed HTML tags. Find if there is a match in each string of the list html_tags. Assign the result to match_tag.
#	If a match is found, print the first group captured and saved in match_tag.
#	If no match is found, complete the regex to match only the text inside the HTML tag. Assign it to notmatch_tag.
#	Print the first group captured by the regex and save it in notmatch_tag.

Hint

#	To capture the text inside <>, place parenthesis around the expression: r"<(text)>. To confirm that the same text appears in the closing tag, reference back to the m group captured by using \m.
#	To print the m group captured, use .group(m).
#	To capture the text inside <>, use parentheses: r"<(text)>.
#	To print the m group captured, use .group(m).

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)
 
    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1))) 
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))
