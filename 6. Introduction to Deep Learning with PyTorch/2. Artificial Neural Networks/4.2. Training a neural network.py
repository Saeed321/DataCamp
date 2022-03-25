•	Instantiate the Adam optimizer with learning rate 3e-4 and instantiate Cross-Entropy as loss function.
•	Complete a forward pass on the neural network using the input data.
•	Using backpropagation, compute the gradients of the weights, and then change the weights using the Adam optimizer.

# Instantiate the network, the Adam optimizer and Cross-Entropy loss function
model = Net()   
optimizer = optim.Adam(model.parameters(), lr=3e-4)
criterion = nn.CrossEntropyLoss()

for batch_idx, data_target in enumerate(train_loader):
    data = data_target[0]
    target = data_target[1]
    data = data.view(-1, 28 * 28)
    optimizer.zero_grad()

    # Complete a forward pass
    output = model(data)

    # Compute the loss, gradients and change the weights
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()
