•	Instantiate two linear layers calling them self.fc1 and self.fc2. Determine their correct dimensions.
•	Implement the .forward() method, using the two layers you defined and returning x.


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        
        # Instantiate all 2 linear layers  
        self.fc1 = nn.Linear(784, 200)
        self.fc2 = nn.Linear(200, 10)

    def forward(self, x):
      
        # Use the instantiated layers and return x
        x = self.fc1(x)
        x = self.fc2(x)
        return x
