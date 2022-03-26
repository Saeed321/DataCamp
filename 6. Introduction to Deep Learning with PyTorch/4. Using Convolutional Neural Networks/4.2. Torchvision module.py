•	Import the module that lets you download state-of-the-art CNNs.
•	Download and load a pretrained ResNet18 network.
•	Freeze all the layers bar the final one.
•	Change the last layer to correspond to the number of classes (7) in your dataset.

# Import the module
import torchvision

# Download resnet18
model = torchvision.models.resnet18(pretrained=True)

# Freeze all the layers bar the last one
for param in model.parameters():
    param.requires_grad = False

# Change the number of output units
model.fc = nn.Linear(512, 7)
