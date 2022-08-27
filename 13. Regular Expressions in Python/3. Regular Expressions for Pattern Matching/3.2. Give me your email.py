
#	Write a regular expression to match valid email addresses as described.
#	Match the regex to the elements contained in emails.
#	To print out the message indicating if it is a valid email or not, complete .format() statement.

Hint

#	To choose between different characters use []. Use a-z for lowercase, A-Z for uppercase letters and 0-9 for numbers. Don't forget to escape . and $ as they have another meaning. Use \w for any word character.
#	To match a pattern to a string, use .match(pattern, string).
#	Remember the .format() syntax: "text {variable}".format(variable=string).

# Write a regex to match a valid email address
regex = r"[A-Za-z0-9!#%&*\$\.]+@\w+\.com"

for example in emails:
  	# Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example))   
