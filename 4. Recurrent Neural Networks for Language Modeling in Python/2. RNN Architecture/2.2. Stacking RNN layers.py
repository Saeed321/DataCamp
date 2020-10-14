# Stacking RNN layers

# Deep RNN models can have tens to hundreds of layers in order to achieve state-of-the-art results.

# In this exercise, you will get a glimpse of how to create deep RNN models by stacking layers of LSTM cells one after the other.
# To do this, you will set the return_sequences argument to True on the firsts two LSTM layers and to False on the last LSTM layer.

# To create models with even more layers, you can keep adding them one after the other or create a function that uses the .add() method 
# inside a loop to add many layers with few lines of code.
# •	Import the LSTM layer.
# •	Return the sequences in the first two layers and don't return the sequences in the last LSTM layer.
# •	Load the pre-trained weights.
# •	Print the loss and accuracy obtained.

# Import the LSTM layer
from keras.layers.recurrent import LSTM

# Build model
model = Sequential()
model.add(LSTM(units=128, input_shape=(None, 1), return_sequences=True))
model.add(LSTM(units=128, return_sequences=True))
model.add(LSTM(units=128, return_sequences=False))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('lstm_stack_model_weights.h5')

print("Loss: %0.04f\nAccuracy: %0.04f" % tuple(model.evaluate(X_test, y_test, verbose=0)))