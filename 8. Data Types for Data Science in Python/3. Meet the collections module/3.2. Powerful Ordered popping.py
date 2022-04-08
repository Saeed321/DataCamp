•	Print the first key in ridership_date (Remember to make keys a list before slicing).
•	Pop the first item from ridership_date and print it.
•	Print the last key in ridership_date.
•	Pop the last item from ridership_date and print it.

# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem(last=True))
