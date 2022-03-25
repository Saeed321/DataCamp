•	Calculate the first and second hidden layer by multiplying the appropriate inputs with the corresponding weights.
•	Calculate and print the results of the output.
•	Set weight_composed_1 to the product of weight_1 with weight_2, then set weight to the product of weight_composed_1 with weight_3.
•	Calculate and print the output.

# Calculate the first and second hidden layer
hidden_1 = torch.matmul(input_layer, weight_1)
hidden_2 = torch.matmul(hidden_1, weight_2)

# Calculate the output
print(torch.matmul(hidden_2, weight_3))

# Calculate weight_composed_1 and weight
weight_composed_1 = torch.matmul(weight_1, weight_2)
weight = torch.matmul(weight_composed_1, weight_3)

# Multiply input_layer with weight
print(torch.matmul(input_layer, weight))
