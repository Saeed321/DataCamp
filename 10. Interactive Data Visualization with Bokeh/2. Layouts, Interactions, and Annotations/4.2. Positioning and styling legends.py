
#	Use p.legend.location to adjust the legend location to be on the 'bottom_left'.
#	Use p.legend.background_fill_color to set the background color of the legend to 'lightgray'.

# Assign the legend to the bottom left: p.legend.location
p.legend.location = 'bottom_left'

# Fill the legend background with the color 'lightgray': p.legend.background_fill_color
p.legend.background_fill_color = 'lightgray'

# Specify the name of the output_file and show the result
output_file('fert_lit_groups.html')
show(p)
