
#	Use the .avg() method to get the average air time of Delta Airlines flights (where the carrier column has the value "DL") that left SEA. The place of departure is stored in the column origin. show() the result.
#	Use the .sum() method to get the total number of hours all planes in this dataset spent in the air by creating a column called duration_hrs from the column air_time. show() the result.

Hint

#	Use two logical conditions to filter the data, one matching the carrier code "DL" and the other matching the airport code SEA.
#	Create the column duration_hrs and pass that as a string to the .sum() method.

# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()
