
#	Create a list of the longitude positions for each state as x. This has already been done for you.
#	Create a list of the latitude positions for each state as y. The variable names for the latitude positions are az_lats, co_lats, nm_lats, and ut_lats.
#	Use the .patches() method to add the patches glyph to the figure p. Supply the x and y lists as arguments along with a line_color of 'white'.

# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
x = [az_lons, co_lons, nm_lons, ut_lons]

# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
y = [az_lats, co_lats, nm_lats, ut_lats]

# Add patches to figure p with line_color=white for x and y
p.patches(x, y, line_color = 'white')

# Specify the name of the output file and show the result
output_file('four_corners.html')
show(p)
