•	Loop over the first 10 items of the datetimes_list, using item as your iterator variable.
	o	Print out the item as a string in the format of 'MM/DD/YYYY'. For this, the format string is '%m/%d/%Y'.
	o	Print out the item as an ISO standard string.

# Loop over the first 10 items of the datetimes_list
for item in datetimes_list[:10]:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(item.strftime('%m/%d/%Y'))
    
    # Print out the record as an ISO standard string
    print(item.isoformat())
