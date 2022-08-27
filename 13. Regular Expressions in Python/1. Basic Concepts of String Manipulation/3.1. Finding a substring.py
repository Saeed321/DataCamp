
#	Find if the substring actor occurs between the characters with index 37and 41 inclusive. If it is not detected, print the statement Word not found.
#	Replace actor actor with the substring actor if actor occurs only two repeated times.
#	Replace actor actor actor with the substring actor if actorappears three repeated times.

Hint

#	Find if a pattern occurs between the characters 1 and 4 (inclusive) of string using string.find(pattern, 1, 5). If not found, .find() will return -1.
#	Count the occurrences of pattern in string using string.count(pattern).
#	Replace old for new in string using string.replace(old, new)

for movie in movies:
  	# Find if actor occurrs between 37 and 41 inclusive
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two by one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences by one
        print(movie.replace("actor actor actor", "actor"))
