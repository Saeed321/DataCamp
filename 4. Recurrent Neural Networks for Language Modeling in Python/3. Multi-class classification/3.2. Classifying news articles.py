# Classifying news articles

# In this exercise you will create a multi-class classification model.
# The dataset is already loaded in the environment as news_novel. 
# Also, all the pre-processing of the training data is already done and tokenizer is also available in the environment.

# A RNN model was pre-trained with the following architecture: use the Embedding layer, one LSTM layer 
# and the output Dense layer expecting three classes: sci.space, alt.atheism, and soc.religion.christian. 
# The weights of this trained model are available on the classify_news_weights.h5 file.

# You will pre-process the novel data and evaluate on a new dataset news_novel.
# •	Transform the data present on news_novel.data using the loaded tokenizer.
# •	Pad the obtained sequences of numerical indexes.
# •	Transform the labels present on news_novel.target into a one-hot representation.
# •	Evaluate the model using the method .evaluate() and print the loss and accuracy obtained.

# Change text for numerical ids and pad
X_novel = tokenizer.texts_to_sequences(news_novel.data)
X_novel = pad_sequences(X_novel, maxlen=400)

# One-hot encode the labels
Y_novel = to_categorical(news_novel.target)

# Load the model pre-trained weights
model.load_weights('classify_news_weights.h5')

# Evaluate the model on the new dataset
loss, acc = model.evaluate(X_novel, Y_novel, batch_size=64)

# Print the loss and accuracy obtained
print("Loss:\t{0}\nAccuracy:\t{1}".format(loss, acc))


