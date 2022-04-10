•	Import Counter from collections and datetime from datetime.
•	Create a Counter object called crimes_by_month.
•	Loop over the crime_data list:
	o	Using the datetime.strptime() function, convert the first element of each item into a Python Datetime Object called date.
	o	Increment the counter for the month associated with this row by one. You can access the month of date using date.month.
•	Print the 3 most common months for crime.


# Import necessary modules
from collections import Counter
from datetime import datetime

# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for row in crime_data:
    
    # Convert the first element of each item into a Python Datetime Object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    
    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
    
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))
