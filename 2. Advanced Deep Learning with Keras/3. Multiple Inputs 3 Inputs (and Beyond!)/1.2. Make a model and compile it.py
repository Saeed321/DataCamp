# Make a model and compile it

# Now that you've input and output layers for the 3-input model, 
# wrap them up in a Keras model class, and then compile the model, 
# so you can fit it to data and use it to make predictions on new data.

# •	Create a model using team_in_1, team_in_2, and home_in as inputs and out as the output.
# •	Compile the model using the 'adam' optimizer and 'mean_absolute_error' as the loss function.

# Import the model class
from keras.models import Model

# Make a Model
model = Model([team_in_1, team_in_2, home_in], out)

# Compile the model
model.compile(optimizer='adam', loss='mean_absolute_error')
