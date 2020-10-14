# Creating the text generation model

# In this exercise, you will define a text generation model using Keras.

# The variables n_vocab containing the vocabulary size and input_shapecontaining the shape of the data used for training are already loaded in the environment. 
# Also, the weights of a pre-trained model is available on file model_weights.h5. The model was trained with 40 epochs on the training data. 
# Recap that to train a model in Keras, you just use the method .fit() on the training data (X, y), and the parameter epochs. For example:
# model.fit(X_train, y_train, epochs=40)
# •	Add one LSTM layer returning the sequences.
# •	Add one LSTM layer not returning the sequences.
# •	Add the output layer with n_vocab units.
# •	Display the model summary.

# Instantiate the model
model = Sequential()

# Add two LSTM layers
model.add(LSTM(64, input_shape=input_shape, dropout=0.15, recurrent_dropout=0.15, return_sequences=True))
model.add(LSTM(64, dropout=0.15, recurrent_dropout=0.15, return_sequences=False))

# Add the output layer
model.add(Dense(n_vocab, activation='softmax'))

# Compile and load weights
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.load_weights('model_weights.h5')
# Summary
model.summary()