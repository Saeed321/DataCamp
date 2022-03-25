•	Multiply tensors x and y, put the product in tensor q.
•	Do an elementwise multiplication of tensors z with q.
•	Calculate the gradients.

# Multiply tensors x and y
q = x * y

# Elementwise multiply tensors z with q
f = torch.matmul(q, z)

mean_f = torch.mean(f)

# Calculate the gradients
mean_f.backward()
