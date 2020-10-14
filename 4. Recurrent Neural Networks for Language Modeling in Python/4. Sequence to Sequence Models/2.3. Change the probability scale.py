# Change the probability scale

# In this exercise, you will see the difference in the resulted sentence when using different values of temperature to scale the probability distribution.

# The function generate_phrase() is an adaptation of the function you created before and is already loaded in the environment. 
# It receives the parameters model with the pre-trained model, initial_text with the context text and 
# temperature that is the value to scale the softmax()function.
# •	Store the list of temperatures to the temperatures variable.
# •	Loop a variable temperature over the temperatures list.
# •	Generate a phrase using the pre-loaded function generate_phrase().
# •	Print the temperature and the generated sentence.

# Define the initial text
initial_text = "Spock and me "

# Define a vector with temperature values
temperatures = [0.2, 0.8, 1.0, 3.0, 10.0]

# Loop over temperatures and generate phrases
for temperature in temperatures:
	# Generate a phrase
	phrase = generate_phrase(model, initial_text, temperature)
    
	# Print the phrase
	print('Temperature {0}: {1}'.format(temperature, phrase))