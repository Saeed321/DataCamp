
#	Import curdoc from bokeh.io and figure from bokeh.plotting.
#	Create a new plot called plot using the figure() function.
#	Add a line to the plot using [1,2,3,4,5] as the x coordinates and [2,5,4,6,7] as the y coordinates.
#	Add the plot to the current document using curdoc().add_root(). It needs to be passed in as an argument to add_root().

# Perform necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure

# Create a new plot: plot
plot = figure()

# Add a line to the plot
plot.line([1,2,3,4,5], [2,5,4,6,7])

# Add the plot to the current document
curdoc().add_root(plot)


