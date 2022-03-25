•	Initialize random tensors x, y and z, each having shape (1000, 1000).
•	Multiply x with y, putting the result in tensor q.
•	Do an elementwise multiplication of tensor z with tensor q, putting the results in f

# Initialize tensors x, y and z
x = torch.rand(1000, 1000)
y = torch.rand(1000, 1000)
z = torch.rand(1000, 1000)

# Multiply x with y
q = x * y

# Multiply elementwise z with q
f = z * q

mean_f = torch.mean(f)
print(mean_f)
