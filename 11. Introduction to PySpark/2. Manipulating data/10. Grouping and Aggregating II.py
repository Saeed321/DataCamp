
#	Import the submodule pyspark.sql.functions as F.
#	Create a GroupedData table called by_month_dest that's grouped by both the month and dest columns. Refer to the two columns by passing both strings as separate arguments.
#	Use the .avg() method on the by_month_dest DataFrame to get the average dep_delay in each month for each destination.
#	Find the standard deviation of dep_delay by using the .agg() method with the function F.stddev().

Hint

#	The .groupBy() method can take as many columns as arguments as you want.
#	Use .agg() by calling grouped_df.agg(F.____("col")).
# Import pyspark.sql.functions as F
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")

# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()