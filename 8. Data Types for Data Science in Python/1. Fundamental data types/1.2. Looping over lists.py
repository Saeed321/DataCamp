•	Create an empty list called baby_names.
•	Use a for loop to iterate over each row of records appending the name, found in the fourth element of row, to baby_names.
•	Print each name in baby_names in alphabetical order. To do this:
•	Use the sorted() function as part of a for loop to iterate over the sorted names, printing each one.

# Create the empty list: baby_names
baby_names = []

# Loop over records 
for row in records:
    # Add the name to the list
    baby_names.append(row[3])
    
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)
