•	Import the datetime object from datetime.
•	Iterate over the dates_list, using date_str as your iterator variable.
•	Convert each date_str into a datetime object called date_dt using the datetime.strptime() function, with '%m/%d/%Y' as your format.
•	Print each date_dt.

# Import the datetime object from datetime
from datetime import datetime

# Iterate over the dates_list 
for date_str in dates_list:
    # Convert each date to a datetime object: date_dt
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')
    
    # Print each date_dt
    print(date_dt)
