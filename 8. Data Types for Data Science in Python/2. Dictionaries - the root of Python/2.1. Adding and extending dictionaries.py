•	Assign the names_2011 dictionary as the value to the 2011 key of the boy_names dictionary.
•	Update the 2012 key in the boy_names dictionary with the following data in a list of tuples: (1, 'Casey'), (2, 'Aiden').
•	Loop over the boy_names dictionary.
	o	Inside the for loop, sort the data for each year of boy_names by descending rank and take the first result which will be the lowest ranked name.
	o	Safely print the year and least popular name or 'Not Available' if it is not found. Take advantage of the .get() method.

# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1,'Casey'), (2,'Aiden')])

# Loop over the years in the boy_names dictionary 
for year in boy_names:
    # sort the data for each year by descending rank and get the lowest one
    lowest_ranked = sorted(boy_names[year], reverse=True)[0]
    # Safely print the year and the least popular name or 'Not Available'
    print(year, boy_names[year].get(lowest_ranked, 'Not Available'))

