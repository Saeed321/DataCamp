# Number of parameters comparison

# You saw that the one-hot representation is not a good representation of words because it is very sparse. 
# Using the Embedding layer creates a dense representation of the vectors, but also demands a lot of parameters to be learned.

# In this exercise you will compare the number of parameters of two models using embeddings and one-hot encoding to see the difference.

# The model model_onehot is already loaded in the environment, as well as the Sequential, Dense and GRU from keras. 
# Finally, the parameters vocabulary_size=80000 and sentence_len=200 are also loaded.
# •	Import the Embedding layer from keras.layers.
# •	On the embedding layer, use vocabulary size plus one as input dimension and sentence size as input length.
# •	Compile the model.
# •	Print the summary of the model with embedding.

# Import the embedding layer
from keras.layers import Embedding

# Create a model with embeddings
model = Sequential(name="emb_model")
model.add(Embedding(input_dim=vocabulary_size + 1, output_dim=wordvec_dim, input_length=sentence_len, trainable=True))
model.add(GRU(128))
model.add(Dense(1))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print the summaries of the one-hot model
model_onehot.summary()

# Print the summaries of the model with embeddings
model.summary()
