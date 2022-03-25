•	Initialize with random numbers two matrices of weights, called weight_1and weight_2.
•	Set the result of input_layer times weight_1 to hidden_1. Set the result of hidden_1 times weight_2 to output_layer.

# Initialize the weights of the neural network
weight_1 = torch.rand(784, 200)  # 784 is input units and 200 is hidden units.
weight_2 = torch.rand(200, 10)   # 200 is hidden units and 10 is output units.

# Multiply input_layer with weight_1
hidden_1 = torch.matmul(input_layer, weight_1)

# Multiply hidden_1 with weight_2
output_layer = torch.matmul(hidden_1, weight_2)
print(output_layer)
