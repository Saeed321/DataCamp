
#	Add a red circle glyph to the figure p using the latin_americaColumnDataSource. Specify a size of 10 and legend of Latin America.
#	Add a blue circle glyph to the figure p using the africaColumnDataSource. Specify a size of 10 and legend of Africa.

Hint

#	You can plot female_literacy vs fertility columns from latin_america using p.circle with source=latin_america, size=10, color='red' and legend='Latin America'.
#	You can plot female_literacy vs fertility columns from africausing p.circle and with source=africa, size=10, color='blue' and legend='Africa'.

# Add the first circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=latin_america, size=10, color='red', legend='Latin America')

# Add the second circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=africa, size=10, color='blue', legend='Africa')

# Specify the name of the output_file and show the result
output_file('fert_lit_groups.html')
show(p)
