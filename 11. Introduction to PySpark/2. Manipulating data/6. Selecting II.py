
# Create a table of the average speed of each flight both ways.
#	Calculate average speed by dividing the distance by the air_time (converted to hours). Use the .alias() method name this column "avg_speed". Save the output as the variable avg_speed.
#	Select the columns "origin", "dest", "tailnum", and avg_speed (without quotes!). Save this as speed1.
#	Create the same table using .selectExpr() and a string containing a SQL expression. Save this as speed2.

# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")
