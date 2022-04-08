•	Import the Python csv module.
•	Create a Python file object in read mode for the baby_names.csv called csvfile.
•	Loop over a csv DictReader on csvfile. Inside the loop:
	o	Print each row.
	o	Add the 'RANK' of each row as the key and 'NAME' of each rowas the value to the existing dictionary.
•	Print the dictionary keys.

# Import the python CSV module
import csv

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('baby_names.csv', 'r')

# Loop over a DictReader on the file
for row in csv.DictReader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row['NAME']

# Print the dictionary keys
print(baby_names.keys())
