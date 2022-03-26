•	Instantiate an object called model from class Net(), which is available in your workspace (consider it as a blackbox).
•	Instantiate the cross-entropy loss.
•	Instantiate Adam optimizer with learning_rate equals to 3e-4, and l2 regularization parameter equals to 0.001.

# Instantiate the network
model = Net()

# Instantiate the cross-entropy loss
criterion = nn.CrossEntropyLoss()

# Instantiate the Adam optimizer
optimizer = optim.Adam(model.parameters(), lr=3e-4, weight_decay=0.001)
