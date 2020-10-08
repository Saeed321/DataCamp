# Is the model overfitting?

# Let's train the model you just built and plot its learning curve to check out if it's overfitting! 
# You can make use of loaded function plot_loss() to plot training loss against validation loss, 
# you can get both from the history callback.

# If you want to inspect the plot_loss() function code, 
# paste this in the console: print(inspect.getsource(plot_loss))
# •	Train your model for 60 epochs, using X_test and y_test as validation data.
# •	Use plot_loss() passing loss and val_loss as extracted from the history attribute of the history object.

# Train your model for 60 epochs, using X_test and y_test as validation data
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), verbose=0, epochs= 60)

# Extract from the history object loss and val_loss to plot the learning curve
plot_loss(history.history['loss'], history.history['val_loss'])

# Question
# Just by looking at the overall picture, do you think the learning curve 
# shows this model is overfitting after having trained for 60 epochs?

# Yes, it started to overfit since the test loss is higher than the training loss.
 
# No, the test loss is not getting higher as the epochs go by.

# Answer : No, the test loss is not getting higher as the epochs go by.