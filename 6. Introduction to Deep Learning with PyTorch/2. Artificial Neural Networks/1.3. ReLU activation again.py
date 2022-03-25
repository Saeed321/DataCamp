•	Instantiate the ReLU() activation function as relu (the function is part of nn module).
•	Initialize weight_1 and weight_2 with random numbers.
•	Multiply the input_layer with weight_1, storing results in hidden_1.
•	Apply the relu activation function over hidden_1, and then multiply the output of it with weight_2.

# Instantiate ReLU activation function as relu
relu = nn.ReLU()

# Initialize weight_1 and weight_2 with random numbers
weight_1 = torch.rand(4, 6)
weight_2 = torch.rand(6, 2)

# Multiply input_layer with weight_1
hidden_1 = torch.matmul(input_layer, weight_1)

# Apply ReLU activation function over hidden_1 and multiply with weight_2
hidden_1_activated = relu(hidden_1)
print(torch.matmul(hidden_1_activated, weight_2))
