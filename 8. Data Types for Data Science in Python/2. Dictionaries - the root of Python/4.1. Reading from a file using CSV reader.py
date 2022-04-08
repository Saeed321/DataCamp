•	Import the python csv module.
•	Create a Python file object in read mode for baby_names.csv called csvfile with the open function.
•	Use the reader method from the csv module on the file object in a for loop. Inside the loop:
	o	Print each row and add the rank (the 6th element of row) as the key and name (the 4th element of row) as the value to the existing dictionary (baby_names).
•	Print the keys of baby_names.

# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('baby_names.csv', 'r')

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary
    baby_names[row[5]] = row[3]

# Print the dictionary keys
print(baby_names.keys())
