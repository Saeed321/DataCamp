
#	Import curdoc from bokeh.io, widgetbox from bokeh.layouts, and Slider from bokeh.models.
#	Create a slider called slider by using the Slider() function and specifying the parameters title, start, end, step, and value.
#	Use the slider to create a widgetbox layout called layout.
#	Add the layout to the current document using curdoc().add_root(). It needs to be passed in as an argument to add_root().

Hint

#	You can import x from y using the command from y import x.
#	You can create a slider using the Slider() function and keyword arguments title='my slider', start=0, end=10, step=0.1, value=2.
#	To create a widgetbox layout, pass slider as an argument to widgetbox().
#	To add the layout to the current document, layout has to be passed in as an argument to add_root() in curdoc().add_root().

# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create a slider: slider
slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)

# Create a widgetbox layout: layout
layout = widgetbox(slider)

# Add the layout to the current document
curdoc().add_root(layout)

