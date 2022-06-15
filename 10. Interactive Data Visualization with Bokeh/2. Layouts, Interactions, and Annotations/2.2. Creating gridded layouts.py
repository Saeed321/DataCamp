
#	Import gridplot from the bokeh.layouts module.
#	Create a list called row1 containing plots p1 and p2.
#	Create a list called row2 containing plots p3 and p4.
#	Create a gridplot using row1 and row2. You will have to pass in row1and row2 in the form of a list.

# Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot

# Create a list containing plots p1 and p2: row1
row1 = [p1, p2]

# Create a list containing plots p3 and p4: row2
row2 = [p3, p4]

# Create a gridplot using row1 and row2: layout
layout = gridplot([row1, row2])

# Specify the name of the output_file and show the result
output_file('grid.html')
show(layout)
