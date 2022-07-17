
#	Import the figure function from bokeh.plotting.
#	Create a figure p using the figure() function with x_axis_type set to 'datetime'. The other two parameters are x_axis_label and y_axis_label.
#	Plot date and price along the x- and y-axes using p.line().

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create a figure with x_axis_type="datetime": p
p = figure(x_axis_type = 'datetime', x_axis_label = 'Date', y_axis_label = 'US Dollars')

# Plot date along the x axis and price along the y axis
p.line(date, price)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)

