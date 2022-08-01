
#	Import SparkSession from pyspark.sql.
#	Make a new SparkSession called my_spark using SparkSession.builder.getOrCreate().
#	Print my_spark to the console to verify it's a SparkSession.

# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
