
#	Create a VectorAssembler by calling VectorAssembler() with the inputCols names as a list and the outputCol name "features".
	#	The list of columns should be ["month", "air_time", "carrier_fact", "dest_fact", "plane_age"].
# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol="features")

