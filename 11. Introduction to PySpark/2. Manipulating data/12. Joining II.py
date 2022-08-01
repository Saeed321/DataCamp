
#	Examine the airports DataFrame by calling .show(). Note which key column will let you join airports to the flights table.
#	Rename the faa column in airports to dest by re-assigning the result of airports.withColumnRenamed("faa", "dest") to airports.
#	Join the flights with the airports DataFrame on the dest column by calling the .join() method on flights. Save the result as flights_with_airports.
	#	The first argument should be the other DataFrame, airports.
	#	The argument on should be the key column.
	#	The argument how should be "leftouter".
#	Call .show() on flights_with_airports to examine the data again. Note the new information that has been added.

# Examine the data
airports.show()

# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, on="dest", how="leftouter")

# Examine the new DataFrame
flights_with_airports.show()
