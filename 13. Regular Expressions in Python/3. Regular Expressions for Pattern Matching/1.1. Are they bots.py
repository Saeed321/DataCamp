
#	Import the re module.
#	Write a regex that matches the user mentions that follows the pattern, e.g. @robot3!.
#	Find all the matches of the pattern in the sentiment_analysis variable.

Hint

#	To import module, use import module.
#	Always start a regex with r. Remember that normal characters match themselves. Use \d to indicate digits and \W to indicate any non-word character, for example, & or #.
#	To find all matches of pattern in a string, use the method .findall() from the re module. Don't forget to specify the pattern and the string as arguments.

# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))
