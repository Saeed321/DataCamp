•	Define a variable, A1, as the 1-dimensional tensor: [1, 2, 3, 4].
•	Print A1. Do not use the .numpy() method. What did this tell you?
•	Apply .numpy() to A1 and assign it to B1.
•	Print B1. What did this tell you?

# Define the 1-dimensional variable A1
A1 = Variable([1, 2, 3, 4])

# Print the variable A1
print(A1)

# Convert A1 to a numpy array and assign it to B1
B1 = A1.numpy()

# Print B1
print(B1)
