# Better sentiment classification

# In this exercise, you go back to the sentiment classification problem seen in Chapter 1.
# You are going to add more complexity to the model and improve its accuracy. 
# You will use an Embedding layer to train word vectors on the training set and two LSTM layers to keep track of longer texts. 
# Also, you will add an extra Dense layer before the output.

# This is no longer a simple model, and the training can take some time. 
# For this reason, a pre-trained model is available by loading its weights with the method .load_weights() from the keras.models.Sequential class. 
# The model was trained with 10 epochs and its weights are available on the file model_weights.h5.

# The following modules are loaded on the environment: Sequential, Embedding, LSTM, Dropout, Dense.
# •	Add an Embedding layer as the first layer of the model.
# •	Add a second LSTM layer with 64 units returning the sequences.
# •	Add an extra Dense layer with 16 units.
# •	Evaluate the model to print the accuracy on the training set.

# Build and compile the model
model = Sequential()
model.add(Embedding(vocabulary_size, wordvec_dim, trainable=True, input_length=max_text_len))
model.add(LSTM(64, return_sequences=True, dropout=0.2, recurrent_dropout=0.15))
model.add(LSTM(64, return_sequences=False, dropout=0.2, recurrent_dropout=0.15))
model.add(Dense(16))
model.add(Dropout(rate=0.25))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('model_weights.h5')

# Print the obtained loss and accuracy
print("Loss: {0}\nAccuracy: {1}".format(*model.evaluate(X_test, y_test, verbose=0)))
