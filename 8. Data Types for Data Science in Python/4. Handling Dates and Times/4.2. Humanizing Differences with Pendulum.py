•	Iterate over the date_ranges list, unpacking it into start_date and end_date. These dates are not in ISO 8601 format.
•	Use pendulum to convert the start_date string to a pendulum date called start_dt.
•	Use pendulum to convert the end_date string to pendulum date called end_dt.
•	Calculate the difference between end_dt and start_dt. Store the result as diff_period.
•	Print the difference in days, using the .in_days() method.


# Iterate over date_ranges
for start_date, end_date in date_ranges:

    # Convert the start_date string to a pendulum date: start_dt 
    start_dt = pendulum.parse(start_date, strict = False)
    
    # Convert the end_date string to a pendulum date: end_dt 
    end_dt = pendulum.parse(end_date, strict = False)
    
    # Print the End and Start Date
    print(end_dt, start_dt)
    
    # Calculate the difference between end_dt and start_dt: diff_period
    diff_period = end_dt - start_dt
    
    # Print the difference in days
    print (diff_period.in_days())
