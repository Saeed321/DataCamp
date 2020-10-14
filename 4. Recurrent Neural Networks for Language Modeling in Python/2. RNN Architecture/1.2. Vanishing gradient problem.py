# Vanishing gradient problem

# The other possible gradient problem is when the gradients vanish, or go to zero. 
# This is a much harder problem to solve because it is not as easy to detect. 
# If the loss function does not improve on every step, is it because the gradients went to zero and thus didn't update the weights? 
# Or is it because the model is not able to learn?

# This problem occurs more often in RNN models when long memory is required, meaning having long sentences.

# In this exercise you will observe the problem on the IMDB data, with longer sentences selected. 
# The data is loaded in X and y variables, as well as classes Sequential, SimpleRNN, Dense and matplotlib.pyplot as plt. 
# The model was pre-trained with 100 epochs and its weights are stored on the file model_weights.h5.
# •	Add a SimpleRNN layer to the model.
# •	Load the pre-trained weights on the model using the method .load_weights().
# •	Add the accuracy of the training data available on the attribute 'acc' to the plot.
# •	Display the plot using the method .show().

# Create the model
model = Sequential()
model.add(SimpleRNN(units=600, input_shape=(None, 1)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('model_weights.h5')

# Plot the accuracy x epoch graph
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['train', 'val'], loc='upper left')
plt.show()
