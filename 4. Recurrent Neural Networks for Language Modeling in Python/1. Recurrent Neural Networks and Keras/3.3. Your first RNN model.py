# Your first RNN model

# In this exercise you will put in practice the Keras modules to build your first RNN model and use it to classify sentiment on movie reviews.

# This first model has one recurrent layer with the vanilla RNN cell: SimpleRNN, 
# and the output layer with two possible values: 0 representing negative sentiment and 1 representing positive sentiment.

# You will use the IMDB dataset contained in keras.datasets. A model was already trained and its weights stored in the file model_weights.h5. 
# You will build the model's architecture and use the pre-loaded variables x_test and y_test to check the its performance.
# •	Add the SimpleRNN cell with 128 units.
# •	Add a Dense layer with one unit for sentiment classification.
# •	Use the proper loss function for binary classification.
# •	Evaluate the model on the pre-trained validation set: (x_test, y_test).

# Build model
model = Sequential()
model.add(SimpleRNN(units=128, input_shape=(None, 1)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', 
              optimizer='adam',
              metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('model_weights.h5')

# Method '.evaluate()' shows the loss and accuracy
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print("Loss: {0} \nAccuracy: {1}".format(loss, acc))
