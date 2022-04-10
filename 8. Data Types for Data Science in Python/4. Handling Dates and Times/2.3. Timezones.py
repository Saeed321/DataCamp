•	Create a Timezone object for Chicago ('US/Central') called chicago_usa_tz.
•	Create a Timezone object for New York ('US/Eastern') called ny_usa_tz.
•	Iterate over the daily_summaries, unpacking it into the variables orig_dt and ridership.
	o	Make the orig_dt timezone "aware" for Chicago, using chicago_usa_tz. Store the result in chicago_dt.
	o	Convert chicago_dt to the New York timezone, ny_dt.
	o	Print the chicago_dt, ny_dt, and ridership.

# Create a Timezone object for Chicago
chicago_usa_tz = timezone('US/Central')

# Create a Timezone object for New York
ny_usa_tz = timezone('US/Eastern')

# Iterate over the daily_summaries list
for orig_dt, ridership in daily_summaries:

    # Make the orig_dt timezone "aware" for Chicago
    chicago_dt = orig_dt.replace(tzinfo=chicago_usa_tz)
    
    # Convert chicago_dt to the New York Timezone
    ny_dt = chicago_dt.astimezone(ny_usa_tz)
    
    # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s, Ridership: %s' % (chicago_dt, ny_dt, ridership))


