•	Initialize the tensor of scores with numbers [[-1.2, 0.12, 4.8]], and the tensor of ground truth [2].
•	Instantiate the cross-entropy loss and call it criterion.
•	Compute and print the loss.

# Initialize the scores and ground truth
logits = torch.tensor([[-1.2, 0.12, 4.8]])
ground_truth = torch.tensor([2])

# Instantiate cross entropy loss
criterion = nn.CrossEntropyLoss()

# Compute and print the loss
loss = criterion(logits, ground_truth)
print(loss)
