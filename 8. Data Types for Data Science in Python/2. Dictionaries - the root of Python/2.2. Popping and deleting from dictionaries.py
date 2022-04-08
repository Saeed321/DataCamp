•	Remove 2011 from female_names and store it as female_names_2011.
•	Safely remove 2015 from female_names with a empty dictionary as the default and store it as female_names_2015. To do this, pass in an empty dictionary {} as a second argument to .pop().
•	Delete 2012 from female_names.
•	Print female_names.


# Remove 2011 from female_names and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 from female_names with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015, {})

# Delete 2012 from female_names
del female_names[2012]

# Print female_names
print(female_names)
