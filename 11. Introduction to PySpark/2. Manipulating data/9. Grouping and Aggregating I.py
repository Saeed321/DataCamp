
#	Create a DataFrame called by_plane that is grouped by the column tailnum.
#	Use the .count() method with no arguments to count the number of flights each plane made.
#	Create a DataFrame called by_origin that is grouped by the column origin.
#	Find the .avg() of the air_time column to find average duration of flights from PDX and SEA.

# Group by tailnum
by_plane = flights.groupBy("tailnum")

# Number of flights each plane made
by_plane.count().show()

# Group by origin
by_origin = flights.groupBy("origin")

# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()
