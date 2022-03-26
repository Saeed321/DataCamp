•	Instantiate two convolutional filters: the first one should have 5 channels, while the second one should have 10 channels. The kernel_size for both of them should be 3, and both should use padding=1. Use the names of the arguments (instead of using 1, use padding=1).
•	Instantiate a ReLU() nonlinearity.
•	Instantiate a max pooling layer which halves the size of the image in both directions.
•	Instantiate a fully connected layer which connects the units with the number of classes (we are using MNIST, so there are 10 classes).

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        
        # Instantiate two convolutional layers
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=5, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=5, out_channels=10, kernel_size=3, padding=1)
        
        # Instantiate the ReLU nonlinearity
        self.relu = nn.ReLU()
        
        # Instantiate a max pooling layer
        self.pool = nn.MaxPool2d(2, 2)
        
        # Instantiate a fully connected layer
        self.fc = nn.Linear(7 * 7 * 10, 10)
