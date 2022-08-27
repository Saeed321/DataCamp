
#	Remove tag <\i> from the end of the string. Print the results.

Hint

#	To remove a char from the end of a string, use string.rstrip(char).

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

#	Split the string contained in movie_tag using the commas as a separating element. Print the results.

Hint

#	To split a string using a char as a separating element, use string.split(char).

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

#	Join back together the list of substring contained in movie_no_commausing whitespace as join elements. Print the results.

Hint

#	To join a list of substring using a char as join elements, use "char".join(list).

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = " ".join(movie_no_comma)
print(movie_join)
