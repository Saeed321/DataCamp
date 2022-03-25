•	Set the network in testing (eval) mode.
•	Put each image into a vector using inputs.view(-1, number_of_features) where the number of features should be deducted by multiplying spatial dimensions (shape) of the image.
•	Do the forward pass and put the predictions in output variable.

# Set the model in eval mode
model.eval()

for i, data in enumerate(test_loader, 0):
    inputs, labels = data
    
    # Put each image into a vector
    inputs = inputs.view(-1, 28 * 28)
    
    # Do the forward pass and get the predictions
    outputs = model(inputs)
    _, outputs = torch.max(outputs.data, 1)
    total += labels.size(0)
    correct += (outputs == labels).sum().item()
print('The testing set accuracy of the network is: %d %%' % (100 * correct / total))
