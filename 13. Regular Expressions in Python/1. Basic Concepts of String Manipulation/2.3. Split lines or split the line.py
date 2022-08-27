
#	Split the string file into many substrings at line boundaries.
#	Print out the resulting variable file_split.
#	Complete the for-loop to split the strings into many substrings using commas as a separator element.

Hint

#	To split a string at line boundaries, use string.splitlines().
#	To print out a variable, use print(variable).
#	To split a string using a char as separator element, use string.split(char).

# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(",")
    print(substring_split)
