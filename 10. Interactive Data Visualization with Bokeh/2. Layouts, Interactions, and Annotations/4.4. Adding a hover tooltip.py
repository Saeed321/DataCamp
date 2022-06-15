
#	Import the HoverTool class from bokeh.models.
#	Use the HoverTool() function to create a HoverTool object called hover and set the tooltips argument to be [('Country','@Country')].
#	Use p.add_tools() with your HoverTool object to add it to the figure.

# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool object: hover
hover = HoverTool(tooltips = [('Country','@Country')]) 

# Add the HoverTool object to figure p
p.add_tools(hover)

# Specify the name of the output_file and show the result
output_file('hover.html')
show(p)
