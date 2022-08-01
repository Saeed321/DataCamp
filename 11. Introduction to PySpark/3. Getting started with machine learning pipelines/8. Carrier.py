
#	Create a StringIndexer called carr_indexer by calling StringIndexer() with inputCol="carrier" and outputCol="carrier_index".
#	Create a OneHotEncoder called carr_encoder by calling OneHotEncoder() with inputCol="carrier_index" and outputCol="carrier_fact".

# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")
