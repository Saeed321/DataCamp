
#	Write a regular expression to match valid passwords as described.
#	Scan the elements in the passwords list to find out if they are valid passwords.
#	To print out the message indicating if it is a valid password or not, complete .format() statement.

Hint

#	To choose between different characters use []. Use a-z for lowercase,A-Z for uppercase letters and 0-9 for numbers. Don't forget to escape . and $. Use the {n, m} quantifier to specify minimum n and maximum m repetitions.
#	To scan the string, use .search() method.
#	Remember the .format() syntax: "text {variable}".format(variable=string).

# Write a regex to match a valid password
regex = r"[A-Za-z0-9!#%&*\$\.]{8,20}" 

for example in passwords:
  	# Scan the strings to find a match
    if re.search(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))     
