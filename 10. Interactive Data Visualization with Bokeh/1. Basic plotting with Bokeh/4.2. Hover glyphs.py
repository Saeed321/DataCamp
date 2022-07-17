
#	Import HoverTool from bokeh.models.
#	Add a circle glyph to the existing figure p for x and y with a size of 10, fill_color of 'grey', alpha of 0.1, line_color of None,hover_fill_color of 'firebrick', hover_alpha of 0.5, and hover_line_color of 'white'.
#	Use the HoverTool() function to create a HoverTool called hover with tooltips=None and mode='vline'.
#	Add the HoverTool hover to the figure p using the p.add_tools()function.

Hint

#	You can import x from y using the command from y import x.
#	Use p.circle() with the arguments x, y, size=10, fill_color='grey', alpha=0.1, line_color=None, hover_fill_color='firebrick', hover_alpha=0.5, hover_line_color='white'.
#	Create the HoverTool hover using the HoverTool() function with tooltips=None, and mode='vline'.
#	Add the HoverTool hover to the figure p by passing it in as an argument to p.add_tools().

# import the HoverTool
from bokeh.models import HoverTool

# Add circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color = 'grey', alpha = 0.1, line_color = None,
         hover_fill_color ='firebrick', hover_alpha = 0.5,
         hover_line_color = 'white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)

