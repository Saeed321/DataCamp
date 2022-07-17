
#	Import HoverTool from bokeh.models.
#	Create a HoverTool object called hover with tooltips=[('Country', '@country')].
#	Add the HoverTool object you created to the plot using add_tools().
#	Create a row layout using widgetbox(slider) and plot.
#	Add the layout to the current document. This has already been done for you.

# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool: hover
hover = HoverTool(tooltips=[('Country', '@country')])

# Add the HoverTool to the plot
plot.add_tools(hover)

# Create layout: layout
layout = row(widgetbox(slider), plot)

# Add layout to current document
curdoc().add_root(layout)
