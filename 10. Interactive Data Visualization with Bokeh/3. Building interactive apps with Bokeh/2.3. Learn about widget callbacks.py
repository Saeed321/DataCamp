
#	Define a callback function callback with the parameters attr, old, new.
#	Read the current value of slider as a variable scale. You can do this using slider.value.
#	Compute values for the updated y using np.sin(scale/x).
#	Update source.data with the new data dictionary. The value for 'x'remains the same, but 'y' should be set to the updated value.
#	Attach the callback to the 'value' property of slider. This can be done using on_change() and passing in 'value' and callback.

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)
