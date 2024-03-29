
#	Make a list of the unique values from the region column. You can use the unique() and tolist() methods on data.region to do this.
#	Import CategoricalColorMapper from bokeh.models and the Spectral6 palette from bokeh.palettes.
#	Use the CategoricalColorMapper() function to make a color mapper called color_mapper with factors=regions_list and palette=Spectral6 (spelled with the letter l, not the number 16).
#	Add the color mapper to the circle glyph as a dictionary with dict(field='region', transform=color_mapper) as the argument passed to the color parameter of plot.circle(). Also set the legend parameter to be the 'region'.
#	Set the legend.location attribute of plot to 'top_right' (i.e. plot.____).

# Make a list of the unique values from the region column: regions_list
regions_list = data.region.unique().tolist()

# Import CategoricalColorMapper from bokeh.models and the Spectral6 palette from bokeh.palettes
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6

# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

# Add the color mapper to the circle glyph
plot.circle(x='x', y='y', fill_alpha=0.8, source=source,
            color=dict(field='region', transform=color_mapper), legend='region')

# Set the legend.location attribute of the plot to 'top_right'
plot.legend.location = 'top_right'

# Add the plot to the current document and add the title
curdoc().add_root(plot)
curdoc().title = 'Gapminder'
