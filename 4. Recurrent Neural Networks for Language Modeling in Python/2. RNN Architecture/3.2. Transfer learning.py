# Transfer learning

# You saw that when training an embedding layer, you need to learn a lot of parameters.

# In this exercise, you will see that when using transfer learning it is possible to use the pre-trained weights and don't update them, 
# meaning that all the parameters of the embedding layer will be fixed, and the model will only need to learn the parameters from the other layers.

# The function load_glove is already loaded on the environment and retrieves the glove matrix as a numpy.ndarray vector. 
# It uses the function covered on the lesson's slides to retrieve the glove vectors with 200 embedding dimensions for the vocabulary present in this exercise.
# •	Use the pre-defined function to load the glove vectors.
# •	Use the initializer Constant on the pre-trained vectors.
# •	Add the output layer as a Dense with one unit.
# •	Print the summary and check the trainable parameters.

# Load the glove pre-trained vectors
glove_matrix = load_glove('glove_200d.zip')

# Create a model with embeddings
model = Sequential(name="emb_model")
model.add(Embedding(input_dim=vocabulary_size + 1, output_dim=wordvec_dim, 
                    embeddings_initializer=Constant(glove_matrix), 
                    input_length=sentence_len, trainable=False))
model.add(GRU(128))
model.add(Dense(1,))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print the summaries of the model with embeddings
model.summary()
