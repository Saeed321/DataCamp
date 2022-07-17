
#	Create a ColumnDataSource called source. Explicitly specify the dataparameter of ColumnDataSource() with {'x': x, 'y': y}.
#	Add a line to the figure plot, with 'x' and 'y' from the ColumnDataSource.
#	Combine the slider and the plot into a column layout called layout. Be sure to first create a widgetbox layout using widgetbox() with slider and pass that into the column() function along with plot.

Hint

#	You can create the ColumnDataSource using the ColumnDataSource()function and specifying the keyword argument data={'x': x, 'y': y}.
#	Inside plot.line(), pass in 'x' and 'y' from the ColumnDataSource object. Be sure to also specify source=source.
#	You can create the column layout using the column() function and passing in the arguments widgetbox(slider) and plot.

# Create ColumnDataSource: source
source = ColumnDataSource(data = {'x': x, 'y': y})

# Add a line to the plot
plot.line('x', 'y', source=source)

# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)
