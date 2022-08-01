
#	Run the query using the .sql() method. Save the result in flight_counts.
#	Use the .toPandas() method on flight_counts to create a pandas DataFrame called pd_counts.
#	Print the .head() of pd_counts to the console.

# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())
