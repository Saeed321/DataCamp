
#	Import the ColumnDataSource class from bokeh.plotting.
#	Use the ColumnDataSource() function to make a new ColumnDataSource object called source from the DataFrame df.
#	Use p.circle() to plot circle glyphs on the figure p with 'Year' on the x-axis and 'Time' on the y-axis.
	#	Make the size of the circles 8, and use color='color' to ensure each glyph is colored by the color column.
	#	Make sure to specify source=source so that the ColumnDataSource object is used.

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p.circle('Year', 'Time', size = 8, color='color', source=source)

# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)
