•	Import defaultdict from collections.
•	Create a defaultdict with a default type of list called ridership.
•	Iterate over the list entries, unpacking it into the variables date, stop, and riders, exactly as you did in the previous exercise.
	o	Use stop as the key of the ridership dictionary and append riders to its value.
•	Print the first 10 items of the ridership dictionary. You can use the .items() method for this. Remember, you have to convert ridership.items() to a list before slicing.


# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)
    
# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])
