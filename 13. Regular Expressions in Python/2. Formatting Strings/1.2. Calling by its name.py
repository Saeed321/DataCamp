
#	Create a dictionary assigning the first and second element appearing in the list courses to the keys "field" and "tool" respectively.

# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

#	Complete the placeholders accessing inside to the elements linked with the keys field and tool in the dictionary data.

#	Print out the resulting message using the .format() method, passing the plan dictionary to replace the data placeholders.

Hint

#	Remember that you can access a value associated to a key in a dictionary inside placeholders using {dictionary[key]}.
#	To pass a dictionary to replace the placeholders in my_message using positional formatting, use my_string.format(p=dictionary) where pis the dictionary used in the placeholders.

# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use dictionary to replace placeholders
print(my_message.format(data=plan))

# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use dictionary to replace placeholders
print(my_message.format(data=plan))
