
#	Create a CrossValidator by calling tune.CrossValidator() with the arguments:
	#	estimator=lr
	#	estimatorParamMaps=grid
	#	evaluator=evaluator
#	Name this object cv.

# Create the CrossValidator
cv = tune.CrossValidator(estimator=lr,
               estimatorParamMaps=grid,
               evaluator=evaluator
               )
