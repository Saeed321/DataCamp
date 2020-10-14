# Transfer learning starting point

# In this exercise you will see the benefit of using pre-trained vectors as a starting point for your model.
# You will compare the accuracy of two models trained with two epochs. 
# The architecture of the models is the same: One embedding layer, 
# one LSTM layer with 128 units and the output layer with 5 units which is the number of classes in the sample data. 
# The difference is that one model uses pre-trained vectors on the embedding layer (transfer learning) and the other doesn't.

# The pre-trained vectors used were the GloVE with 200 dimension. 
# The training accuracy history of the validation set of both models are available in the variables history_no_emb and history_emb.
# •	Import module matplotlib.pyplot as plt.
# •	Add the list of accuracy from the model without embeddings to the plot.
# •	Add the list of accuracy from the model with embeddings to the plot.
# •	Display the plot using the method .show().

# Import plotting package
import matplotlib.pyplot as plt

# Insert lists of accuracy obtained on the validation set
plt.plot(history_no_emb['acc'], marker='o')
plt.plot(history_emb['acc'], marker='o')

# Add extra descriptions to plot
plt.title('Learning with and without pre-trained embedding vectors')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['no_embeddings', 'with_embeddings'], loc='upper left')

# Display the plot
plt.show()
