
#	Create the figure p with the figure() function. It has two parameters: x_axis_label and y_axis_label.
#	Add a circle glyph to the figure p using the function p.circle() where the inputs are the x and y data from Latin America: fertility_latinamerica and female_literacy_latinamerica.
#	Add an x glyph to the figure p using the function p.x() where the inputs are the x and y data from Africa: fertility_africa and female_literacy_africa.
#	The code to create, display, and specify the name of the output file has been written for you, so after adding the x glyph, hit 'Submit Answer' to view the figure.

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica)

# Add an x glyph to the figure p
p.x(fertility_africa, female_literacy_africa)

# Specify the name of the file
output_file('fert_lit_separate.html')

# Display the plot
show(p)
