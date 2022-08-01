
#	Use the DataFrame method .randomSplit() to split piped_data into two pieces, training with 60% of the data, and test with 40% of the data by passing the list [.6, .4] to the .randomSplit() method.

# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])
