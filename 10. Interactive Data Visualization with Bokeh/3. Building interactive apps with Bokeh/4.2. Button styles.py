
#	Import CheckboxGroup, RadioGroup, Toggle from bokeh.models.
#	Add a Toggle called toggle using the Toggle() function with button_type 'success' and label 'Toggle button'.
#	Add a CheckboxGroup called checkbox using the CheckboxGroup()function with labels=['Option 1', 'Option 2', 'Option 3'].
#	Add a RadioGroup called radio using the RadioGroup() function with labels=['Option 1', 'Option 2', 'Option 3'].
#	Add a widgetbox containing the Toggle toggle, CheckboxGroup checkbox, and RadioGroup radio to the current document.

# Import CheckboxGroup, RadioGroup, Toggle from bokeh.models
from bokeh.models import CheckboxGroup, RadioGroup, Toggle

# Add a Toggle: toggle
toggle = Toggle(button_type = 'success', label = 'Toggle button')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
curdoc().add_root(widgetbox(toggle, checkbox, radio))
