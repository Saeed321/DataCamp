
#	Import the re module.
#	Write a regex expression to replace HTML tags with an empty string.
#	Print out the result.

Hint

#	Write a regex that looks for any character one or more times but uses a lazy quantifier by appending ?. Use it inside the function re.sub(regex,replacement, string).

# Import re
import re

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

# Print out the result
print(string_notags)
