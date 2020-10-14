# Using the CNN layer

# In this exercise, you will use a pre-trained model that makes use of the Conv1D and MaxPooling1D layers from the keras.layers.convolutional module, 
# and achieves even better accuracy on the classification task.

# This architecture achieved good results in language modeling tasks such as classification, 
# and is added here as an extra exercise to see it in action and have some intuitions.
# Because this layer is not in the scope of the course, you will focus on how to use the layers together with the RNN layers you already learned.

# Please follow the instructions to see the results.
# •	Print the model's architecture.
# •	Load the pre-trained weights.
# •	Evaluate the model on the test data.

# Print the model summary
model_cnn.summary()

# Load pre-trained weights
model_cnn.load_weights('model_weights.h5')

# Evaluate the model to get the loss and accuracy values
loss, acc = model_cnn.evaluate(x_test, y_test, verbose=0)

# Print the loss and accuracy obtained
print("Loss: {0}\nAccuracy: {1}".format(loss, acc))
