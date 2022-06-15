
#	Import row and column from bokeh.layouts.
#	Create a row layout called row2 with the figures mpg_hp and mpg_weight in a list and set sizing_mode='scale_width'.
#	Create a column layout called layout with the figure avg_mpg and the row layout row2 in a list and set sizing_mode='scale_width'.

# Import column and row from bokeh.layouts
from bokeh.layouts import row, column

# Make a row layout that will be used as the second row: row2
row2 = row([mpg_hp, mpg_weight], sizing_mode='scale_width')

# Make a column layout that includes the above row layout: layout
layout = column([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)
