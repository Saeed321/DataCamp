
#	Import the submodule pyspark.ml.evaluation as evals.
#	Create evaluator by calling evals.BinaryClassificationEvaluator() with the argument metricName="areaUnderROC".

# Import the evaluation submodule
import pyspark.ml.evaluation as evals

# Create a BinaryClassificationEvaluator
evaluator = evals.BinaryClassificationEvaluator(metricName="areaUnderROC")
