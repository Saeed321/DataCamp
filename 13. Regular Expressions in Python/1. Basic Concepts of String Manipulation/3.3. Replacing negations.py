
#	Replace the substring isn't for the word is.
#	Replace the substring important for the word insignificant.
#	Print out the result contained in the variable movies_antonym.

Hint

#	To replace a substr1 by other new_substr in a string use string.replace(substr, new_substr). Remember to use double quotes so that the single quotes in isn't does not interfere.
#	To print new_string use print(new_string).

# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)
