
#	Use the method .withColumn() to .cast() the following columns to type "integer". Access the columns using the df.col notation:
	#	model_data.arr_delay
	#	model_data.air_time
	#	model_data.month
	#	model_data.plane_year

# Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time", model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast("integer"))
