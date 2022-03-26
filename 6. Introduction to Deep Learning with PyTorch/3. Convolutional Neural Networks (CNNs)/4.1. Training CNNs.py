•	Compute the predictions from the net.
•	Using the predictions and the labels, compute the loss function.
•	Compute the gradients for each weight.
•	Update the weights using the optimizer.

for i, data in enumerate(train_loader, 0):
    inputs, labels = data
    optimizer.zero_grad()

    # Compute the forward pass
    outputs = net(inputs)
        
    # Compute the loss function
    loss = criterion(outputs, labels)
        
    # Compute the gradients
    loss.backward()
    
    # Update the weights
    optimizer.step()
