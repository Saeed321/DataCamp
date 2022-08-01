#	Create the column plane_age using the .withColumn() method and subtracting the year of manufacture (column plane_year) from the year (column year) of the flight.

Hint

#	You can subtract two columns by typing df.col1 - df.col2.
#	Make sure you are computing the age of the plane as the year of the flight minus the year of the plane manufacture.

# Create the column plane_age
model_data = model_data.withColumn("plane_age", model_data.year - model_data.plane_year)

