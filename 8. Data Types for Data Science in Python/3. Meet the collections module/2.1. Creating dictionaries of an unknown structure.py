•	Create an empty dictionary called ridership.
•	Iterate over entries, unpacking it into the variables date, stop, and riders.
•	Check to see if the date already exists in the ridership dictionary. If it does not exist, create an empty list for the date key.
•	Append a tuple consisting of stop and riders to the date key of the ridership dictionary.
•	Print the ridership for '03/09/2016'.

# Create an empty dictionary: ridership
ridership = {}

# Iterate over the entries
for date, stop, riders in entries:
    # Check to see if date is already in the ridership dictionary
    if date not in ridership:
        # Create an empty list for any missing date
        ridership[date] = []
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop, riders))
    
# Print the ridership for '03/09/2016'
print(ridership['03/09/2016'])
