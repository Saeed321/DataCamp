
#	The code to create a pandas DataFrame of random numbers has already been provided and saved under pd_temp.
#	Create a Spark DataFrame called spark_temp by calling the .createDataFrame() method with pd_temp as the argument.
#	Examine the list of tables in your Spark cluster and verify that the new DataFrame is not present. Remember you can use spark.catalog.listTables() to do so.
#	Register spark_temp as a temporary table named "temp" using the .createOrReplaceTempView() method. Remember that the table name is set including it as the only argument!
#	Examine the list of tables again!



# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp)

# Examine the tables in the catalog
print(spark.catalog.listTables())

# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")

# Examine the tables in the catalog again
print(spark.catalog.listTables())
