
#	Import CategoricalColorMapper from bokeh.models.
#	Convert the DataFrame df to a ColumnDataSource called source. This has already been done for you.
#	Make a CategoricalColorMapper object called color_mapper with the CategoricalColorMapper() function. It has two parameters here: factors and palette.
#	Add a circle glyph to the figure p to plot 'mpg' (on the y-axis) vs 'weight' (on the x-axis). Remember to pass in source and 'origin'as arguments to source and legend. For the color parameter, use dict(field='origin', transform=color_mapper).

#Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])

# Add a circle glyph to the figure p
p.circle('weight', 'mpg', source=source,
            color=dict(field='origin', transform=color_mapper),
            legend='origin')

# Specify the name of the output file and show the result
output_file('colormap.html')
show(p)
