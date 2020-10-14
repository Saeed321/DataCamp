# GRU cells are better than simpleRNN

# In this exercise you will re-run the same model as the first chapter of the course to compare the accuracy of the model by 
# simpling changing the SimpleRNNcell to a GRU cell.

# The model was already trained with 10 epochs, as in the previous model with a SimpleRNN cell. 
# In order to compare the models, a test set (x_test, y_test) is already loaded in the environment, as well as the old model SimpleRNN_model.
# •	Import the GRU cell.
# •	Print the models' summaries.
# •	Print the accuracy of each model.

# Import the modules
from keras.layers import GRU, Dense

# Print the old and new model summaries
SimpleRNN_model.summary()
gru_model.summary()

# Evaluate the models' performance (ignore the loss value)
_, acc_simpleRNN = SimpleRNN_model.evaluate(X_test, y_test, verbose=0)
_, acc_GRU = gru_model.evaluate(X_test, y_test, verbose=0)

# Print the results
print("SimpleRNN model's accuracy:\t{0}".format(acc_simpleRNN))
print("GRU model's accuracy:\t{0}".format(acc_GRU))

