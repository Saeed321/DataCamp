•	Initialize tensors x, y and z to values 4, -3 and 5.
•	Put the sum of tensors x and y in q, put the product of q and z in f.
•	Calculate the derivatives of the computational graph.
•	Print the gradients of the x, y and z tensors.

# Initialize x, y and z to values 4, -3 and 5
x = torch.tensor(4., requires_grad=True)
y = torch.tensor(-3., requires_grad=True)
z = torch.tensor(5., requires_grad=True)

# Set q to sum of x and y, set f to product of q with z
q = x + y
f = q * z

# Compute the derivatives
f.backward()

# Print the gradients
print("Gradient of x is: " + str(x.grad))
print("Gradient of y is: " + str(y.grad))
print("Gradient of z is: " + str(z.grad))
