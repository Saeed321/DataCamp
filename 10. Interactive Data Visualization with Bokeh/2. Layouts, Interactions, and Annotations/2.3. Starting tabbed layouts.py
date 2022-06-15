
#	Import Panel from bokeh.models.widgets.
#	Create a new panel tab1 with child p1 and a title of 'Latin America'.
#	Create a new panel tab2 with child p2 and a title of 'Africa'.
#	Create a new panel tab3 with child p3 and a title of 'Asia'.
#	Create a new panel tab4 with child p4 and a title of 'Europe'.
#	Click submit to check your work.

# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Panel

# Create tab1 from plot p1: tab1
tab1 = Panel(child=p1, title='Latin America')

# Create tab2 from plot p2: tab2
tab2 = Panel(child=p2, title='Africa')

# Create tab3 from plot p3: tab3
tab3 = Panel(child=p3, title='Asia')

# Create tab4 from plot p4: tab4
tab4 = Panel(child=p4, title='Europe')
