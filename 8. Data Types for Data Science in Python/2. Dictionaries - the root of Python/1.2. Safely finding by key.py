•	Safely print rank 7 from the names dictionary.
•	Safely print the type of rank 100 from the names dictionary.
•	Safely print rank 105 from the names dictionary or 'Not Found' if 105 is not found.


# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.get(105, 'Not Found'))
