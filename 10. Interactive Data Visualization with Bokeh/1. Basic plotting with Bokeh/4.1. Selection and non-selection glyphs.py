
#	Create a figure p with an x-axis label of 'Year', y-axis label of 'Time', and the 'box_select' tool. To add the 'box_select' tool, you have to specify the keyword argument tools='box_select' inside the figure() function.
#	Now that you have added 'box_select' to p, add in circle glyphs with p.circle() such that the selected glyphs are red and non-selected glyphs are transparent blue. This can be done by specifying 'red' as the argument to selection_color and 0.1 to nonselection_alpha. Remember to also pass in the arguments for the x ('Year'), y ('Time'), and source parameters of p.circle().
#	Click 'Submit Answer' to output the file and show the figure.

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label = 'Year', y_axis_label = 'Time', tools='box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle('Year', 'Time', selection_color = 'red', nonselection_alpha = 0.1, source = source)

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)
