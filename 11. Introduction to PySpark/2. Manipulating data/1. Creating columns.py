
#	Use the spark.table() method with the argument "flights" to create a DataFrame containing the values of the flights table in the .catalog. Save it as flights.
#	Show the head of flights using flights.show(). The column air_time contains the duration of the flight in minutes.
#	Update flights to include a new column called duration_hrs, that contains the duration of each flight in hours.

# Create the DataFrame flights
flights = spark.table("flights")

# Show the head
flights.show()

# Add duration_hrs
flights = flights.withColumn("duration_hrs", flights.air_time/60)
