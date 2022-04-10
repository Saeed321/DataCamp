•	Create a Python file object in read mode for crime_sampler.csv called csvfile.
•	Create a dictionary that defaults to a list called crimes_by_district.
•	Loop over a DictReader of the CSV file:
	o	Pop 'District' from each row and store it as district.
	o	Append the rest of the data (row) to the district key of crimes_by_district.


# Create the CSV file: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create a dictionary that defaults to a list: crimes_by_district
crimes_by_district = defaultdict(list)

# Loop over a DictReader of the CSV file
for row in csv.DictReader(csvfile):
    # Pop the district from each row: district
    district = row.pop('District')
    # Append the rest of the data to the list for proper district in crimes_by_district
    crimes_by_district[district].append(row)
