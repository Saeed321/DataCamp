
#	Import the figure function from bokeh.plotting, and the output_file and show functions from bokeh.io.
#	Create the figure p with figure(). It has two parameters: x_axis_label and y_axis_label.
#	Add a circle glyph to the figure p using the function p.circle() where the inputs are, in order, the x-axis data and y-axis data.
#	Use the output_file() function to specify the name 'fert_lit.html'for the output file.
#	Create and display the output file using show() and passing in the figure p.

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility, female_literacy)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)

