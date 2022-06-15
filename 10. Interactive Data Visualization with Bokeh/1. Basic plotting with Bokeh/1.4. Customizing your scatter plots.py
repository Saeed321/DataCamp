
#	Using the Latin America data (fertility_latinamerica and female_literacy_latinamerica), add a blue circle glyph of size=10 and alpha=0.8 to the figure p. To do this, you will need to specify the color, size and alpha keyword arguments inside p.circle().
#	Using the Africa data (fertility_africa and female_literacy_africa), add a red circle glyph of size=10 and alpha=0.8 to the figure p.

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color = 'blue', size = 10, alpha = 0.8)

# Add a red circle glyph to the figure p
p.circle(fertility_africa, female_literacy_africa, color = 'red', size = 10, alpha = 0.8)

# Specify the name of the file
output_file('fert_lit_separate_colors.html')

# Display the plot
show(p)
