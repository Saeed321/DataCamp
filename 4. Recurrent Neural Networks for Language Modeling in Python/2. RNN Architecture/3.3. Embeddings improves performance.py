# Embeddings improves performance

# Does the embedding layer improves the accuracy of the model? Let's check it out in the same IMDB data.
# The model was already trained with 10 epochs, as in the previous model with simpleRNN cell. 
# In order to compare the models, a test set (X_test, y_test) is available in the environment, as well as the old model simpleRNN_model. 
# The old model's accuracy is loaded in the variable acc_SimpleRNN.

# All required modules and functions as loaded in the environment: Sequential() from keras.models, 
# Embedding and Dense from keras.layers and SimpleRNN from keras.layers.recurrent.
# •	Add the embedding layer to the model.
# •	Compute the model's accuracy and store on the variable acc_embeddings.
# •	Print the accuracy of the old and new models.

# Create the model with embedding
model = Sequential(name="emb_model")
model.add(Embedding(input_dim=max_vocabulary, output_dim=wordvec_dim, input_length=max_len))
model.add(SimpleRNN(units=128))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('embedding_model_weights.h5')

# Evaluate the models' performance (ignore the loss value)
_, acc_embeddings = model.evaluate(X_test, y_test, verbose=0)

# Print the results
print("SimpleRNN model's accuracy:\t{0}\nEmbeddings model's accuracy:\t{1}".format(acc_simpleRNN, acc_embeddings))
