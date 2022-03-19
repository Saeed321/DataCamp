•	Import numpy and tensorflow under their standard aliases.
•	Use a numpy array to set the tensor price to have a data type of 32-bit floating point number
•	Use the tensorflow function cast() to set the tensor waterfront to have a Boolean data type.
•	Print price and then waterfront. Did you notice any important differences?

# Import numpy and tensorflow with their standard aliases
import numpy as np
import tensorflow as tf

# Use a numpy array to define price as a 32-bit float
price = np.array(housing['price'], np.float32)

# Define waterfront as a Boolean using cast
waterfront = tf.cast(housing['waterfront'], tf.bool)

# Print price and waterfront
print(price)
print(waterfront)
