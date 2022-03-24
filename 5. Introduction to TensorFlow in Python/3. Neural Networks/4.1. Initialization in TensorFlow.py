•	Initialize the layer 1 weights, w1, as a Variable() with shape [23, 7], drawn from a normal distribution.
•	Initialize the layer 1 bias using ones.
•	Use a draw from the normal distribution to initialize w2 as a Variable()with shape [7, 1].
•	Define b2 as a Variable() and set its initial value to 0.0.

# Define the layer 1 weights
w1 = Variable(random.normal([23, 7]))

# Initialize the layer 1 bias
b1 = Variable(ones([7]))

# Define the layer 2 weights
w2 = Variable(random.normal([7, 1]))

# Define the layer 2 bias
b2 = Variable(([0.0]))
