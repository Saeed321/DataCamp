•	Import the Python csv module.
•	Create a Python file object in read mode for crime_sampler.csv called csvfile.
•	Create an empty list called crime_data.
•	Loop over a csv reader on the file object :
	o	Inside the loop, append the date (first element), type of crime (third element), location description (fifth element), and arrest (sixth element) to the crime_data list.
•	Remove the first element (headers) from the crime_data list.
•	Print the first 10 records of the crime_data list. This has been done for you, so hit 'Submit Answer' to see the result!

# Import the csv module
import csv 

# Create the file object: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create an empty list: crime_data
crime_data = []

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):

    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[0], row[2], row[4], row[5]))
    
# Remove the first element from crime_data
crime_data.pop(0)

# Print the first 10 records
print(crime_data[:10])
