
#	Import Pipeline from pyspark.ml.
#	Call the Pipeline() constructor with the keyword argument stages to create a Pipeline called flights_pipe.
	#	stages should be a list holding all the stages you want your data to go through in the pipeline. Here this is just: [dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler]

# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])
