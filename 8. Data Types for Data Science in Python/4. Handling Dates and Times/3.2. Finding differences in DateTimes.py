•	Iterate over date_ranges, unpacking it into start_date and end_date.
	o	Print the end_date and start_date using the same print()function.
	o	Print the difference between each end_date and start_date.

# Iterate over the date_ranges
for start_date, end_date in date_ranges:
    # Print the End and Start Date
    print(end_date, start_date)
    # Print the difference between each end and start date
    print(end_date - start_date)

