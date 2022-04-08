•	Print the keys of the boy_names dictionary.
•	Print the keys of the boy_names dictionary for the year 2013.
•	Loop over the boy_names dictionary.
	o	Inside the loop, safely print the year and the third ranked name. Print 'Unknown' if the third ranked name is not found.

# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, 'Unknown'))
