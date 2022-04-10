•	Import defaultdict from collections and datetime from datetime.
•	Create a dictionary that defaults to a list called locations_by_month.
•	Loop over the crime_data list:
	o	Convert the first element to a date object exactly like you did in the previous exercise.
	o	If the year is 2016, set the key of locations_by_month to be the month of date and .append() the location (fifth element of row) to the values list.
•	Print the dictionary. This has been done for you, so hit 'Submit Answer' to see the result!

# Import necessary modules
from collections import defaultdict
from datetime import datetime

# Create a dictionary that defaults to a list: locations_by_month
locations_by_month = defaultdict(list)

# Loop over the crime_data list
for row in crime_data:
    # Convert the first element to a date object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    
    # If the year is 2016 
    if date.year == 2016:
        # Set the dictionary key to the month and append the location (fifth element) to the values list
       locations_by_month[date.month].append(row[4])
    
# Print the dictionary
print(locations_by_month)
