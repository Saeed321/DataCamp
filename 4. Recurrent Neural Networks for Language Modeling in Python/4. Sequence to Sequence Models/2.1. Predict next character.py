# Predict next character

# In this exercise, you will code the function to predict the next character given a trained model. 
# You will use the past 20 chars to predict the next one. 
# You will learn how to train the model in the next lesson, as this step is integral before model training.

# This is the initial step to create rules for generating sentences, paragraphs, short texts or other blocks of text as needed.
# The variables n_vocab, chars_window and the dictionary index_to_char are already loaded in the environment. 
# Also, the functions below are already created for you:
# •	initialize_X(): Transforms the text input into a sequence of index numbers with the correct shape.
# •	predict_next_char(): Gets the next character using the .predict() method of the model class and the index_to_chardictionary.
# •	Define the function get_next_char() and add the parameters initial_text and chars_window without default values.
# •	Use initialize_X() function and pass variable char_to_index to obtain a vector of zeros to be used for prediction.
# •	Use the predict_next_char() function to obtain the prediction and store it in the next_char variable.
# •	Print the predicted character by applying the defined function on the given initial_text.

def get_next_char(model, initial_text, chars_window, char_to_index, index_to_char):
  	# Initialize the X vector with zeros
    X = initialize_X(initial_text, chars_window, char_to_index)
    
    # Get next character using the model
    next_char = predict_next_char(model, X, index_to_char)
	
    return next_char

# Define context sentence and print the generated text
initial_text = "I am not insane, "
print("Next character: {0}".format(get_next_char(model, initial_text, 20, char_to_index, index_to_char)))