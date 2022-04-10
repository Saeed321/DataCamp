•	Create a defaultdict of an integer called monthly_total_rides.
•	Loop over the list daily_summaries, which contains the columns mentioned above in the assignment text.
	o	Convert the service_date (1st element of daily_summary) to a datetime object called service_datetime. Use '%m/%d/%Y' as your format string.
	o	Use the month of the service_datetime as the dict key and add the total_rides (5th element of daily_summary) to the current amount for the month. Be sure to convert this into an integer.
•	Print monthly_total_rides.

# Create a defaultdict of an integer: monthly_total_rides
monthly_total_rides = defaultdict(int)

# Loop over the list daily_summaries
for daily_summary in daily_summaries:
    # Convert the service_date to a datetime object
    service_datetime = datetime.strptime(daily_summary[0], '%m/%d/%Y')

    # Add the total rides to the current amount for the month
    monthly_total_rides[service_datetime.month] += int(daily_summary[4])
    
# Print monthly_total_rides
print(monthly_total_rides)
