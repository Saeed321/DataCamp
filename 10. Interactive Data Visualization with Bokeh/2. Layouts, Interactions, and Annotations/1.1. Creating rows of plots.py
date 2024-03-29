
#	Import row from the bokeh.layouts module.
#	Create a new figure p1 using the figure() function and specifying the two parameters x_axis_label and y_axis_label.
#	Add a circle glyph to p1. The x-axis data is 'fertility' and y-axis data is 'female_literacy'. Be sure to also specify source=source.
#	Create a new figure p2 using the figure() function and specifying the two parameters x_axis_label and y_axis_label.
#	Add a circle() glyph to p2, specifying the x and y parameters.
#	Put p1 and p2 into a horizontal layout using row().
#	Click 'Submit Answer' to output the file and show the figure.

Hint

#	You can import x from y using the command from y import x.
#	You can create p1 using figure() with x_axis_label = 'fertility (children per woman)' and y_axis_label = 'female_literacy (% population)'.
#	To add a circle glyph to p1, use p1.circle() with 'fertility', 'female_literacy' and source=source as arguments.
#	You can create p2 using figure() with x_axis_label = 'population' and y_axis_label = 'female_literacy (% population)'.
#	To add a circle glyph to p2, use p2.circle() with 'population', 'female_literacy' and source=source as arguments.
#	You can put p1 and p2 into a horizontal layout using row().

# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p1
p1.circle('fertility', 'female_literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p2
p2.circle('population', 'female_literacy', source=source)

# Put p1 and p2 into a horizontal row: layout
layout = row(p1, p2)

# Specify the name of the output_file and show the result
output_file('fert_row.html')
show(layout)
