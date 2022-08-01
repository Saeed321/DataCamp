
#	Use the .read.csv() method to create a Spark DataFrame called airports
	#	The first argument is file_path
	#	Pass the argument header=True so that Spark knows to take the column names from the first line of the file.
#	Print out this DataFrame by calling .show().

# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()
