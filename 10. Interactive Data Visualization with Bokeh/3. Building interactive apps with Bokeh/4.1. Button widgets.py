
#	Create a button called button using the function Button() with the label 'Update Data'.
#	Define an update callback update() with no arguments.
#	Compute new y values using the code provided.
#	Update the ColumnDataSource data dictionary source.data with the new 'y' value.
#	Add the update callback to the button using on_click().

# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x': x, 'y': y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)
