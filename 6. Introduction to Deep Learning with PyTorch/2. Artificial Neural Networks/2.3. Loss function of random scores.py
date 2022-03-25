•	Import torch and torch.nn as nn
•	Initialize logits with a random tensor of shape (1, 1000) and ground_truth with a tensor containing the number 111.
•	Instantiate the cross-entropy loss in a variable called criterion.
•	Calculate and print the loss function.

# Import torch and torch.nn
import torch
import torch.nn as nn

# Initialize logits and ground truth
logits = torch.rand(1, 1000)
ground_truth = torch.tensor([111])

# Instantiate cross-entropy loss
criterion = nn.CrossEntropyLoss()

# Calculate and print the loss
loss = criterion(logits, ground_truth)
print(loss)
