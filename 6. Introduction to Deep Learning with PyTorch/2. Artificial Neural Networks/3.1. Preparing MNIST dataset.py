•	Transform the data to torch tensors and normalize it, mean is 0.1307while std is 0.3081.
•	Prepare the trainset and the testset.
•	Prepare the dataloaders for training and testing so that only 32 pictures are processed at a time.

# Transform the data to torch tensors and normalize it 
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307), ((0.3081)))])

# Prepare training set and testing set
trainset = torchvision.datasets.MNIST('mnist', train=True, download=True, transform= transform)
testset = torchvision.datasets.MNIST('mnist', train=False, download=True, transform= transform)

# Prepare training loader and testing loader
trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True, num_workers=0)
testloader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=False, num_workers=0)
