
#	Import Tabs from bokeh.models.widgets.
#	Create a Tabs layout called layout with tab1, tab2, tab3, and tab4.
#	Click 'Submit Answer' to output the file and show the figure.

# Import Tabs from bokeh.models.widgets
from bokeh.models.widgets import Tabs

# Create a Tabs layout: layout
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

# Specify the name of the output_file and show the result
output_file('tabs.html')
show(layout)

