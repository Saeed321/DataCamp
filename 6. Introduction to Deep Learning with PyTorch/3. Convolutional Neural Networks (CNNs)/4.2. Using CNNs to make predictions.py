•	Iterate over the given test_loader, saving the results of each iteration in data.
•	Get the image and label from the data tuple, storing the results in imageand label.
•	Make a forward pass in the net using your image.
•	Get the net prediction using torch.max() function.

# Iterate over the data in the test_loader
for i, data in enumerate(test_loader):
  
    # Get the image and label from data
    image, label = data
    
    # Make a forward pass in the net with your image
    output = net(image)
    
    # Argmax the results of the net
    _, predicted = torch.max(output.data, 1)
    if predicted == label:
        print("Yipes, your net made the right prediction " + str(predicted))
    else:
        print("Your net prediction was " + str(predicted) + ", but the correct label is: " + str(label))
