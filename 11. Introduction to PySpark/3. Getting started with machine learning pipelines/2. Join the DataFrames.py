
#	First, rename the year column of planes to plane_year to avoid duplicate column names.
#	Create a new DataFrame called model_data by joining the flights table with planes using the tailnum column as the key.

# Rename year column
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(planes, on="tailnum", how="leftouter")
