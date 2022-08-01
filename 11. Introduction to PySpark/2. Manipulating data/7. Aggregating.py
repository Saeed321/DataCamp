
#	Find the length of the shortest (in terms of distance) flight that left PDX by first .filter()ing and using the .min() method. Perform the filtering by referencing the column directly, not passing a SQL string.
#	Find the length of the longest (in terms of time) flight that left SEA by filter()ing and using the .max() method. Perform the filtering by referencing the column directly, not passing a SQL string.

Hint

#	Make sure that you pass a logical column as an argument to filter (e.g. filter(df.col < 2)), not a string.
#	The .min() and .max() methods, however, take the name of a column as a string, e.g. max("col").

# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()
