
#	Use the .filter() method to find all the flights that flew over 1000 miles two ways:
	#	First, pass a SQL string to .filter() that checks whether the distance is greater than 1000. Save this as long_flights1.
	#	Then pass a column of boolean values to .filter() that checks the same thing. Save this as long_flights2.
#	Use .show() to print heads of both DataFrames and make sure they're actually equal!

# Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")

# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)

# Print the data to check they're equal
long_flights1.show()
long_flights2.show()
