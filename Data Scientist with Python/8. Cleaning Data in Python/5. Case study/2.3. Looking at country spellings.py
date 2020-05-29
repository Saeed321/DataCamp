# Looking at country spellings

# Having tidied your DataFrame and checked the data types, your next task in the data cleaning process is to look at the 'country' column to see if there are any special or invalid characters you may need to deal with.
# It is reasonable to assume that country names will contain:
# �	The set of lower and upper case letters.
# �	Spaces between words.
# �	Periods for any abbreviations.

# To confirm that this is the case, you can leverage the power of regular expressions again. For common operations like this, Pandas has a built-in string method - str.contains() - which takes a regular expression pattern, and applies it to the Series, returning True if there is a match, and Falseotherwise.
# Since here you want to find the values that do not match, you have to invert the boolean, which can be done using ~. This Boolean series can then be used to get the Series of countries that have invalid names.
# pandas is loaded and gapminder is available.

# Instructions

# Using the country column of gapminder, drop the duplicate names, then locate the countries that do not contain only one or more (lower and upper case) letters, spaces, and periods. Assign this to invalid_countries and print.

# Print invalid_countries, a list of countries that doesn't 
# contain only letters, periods, and spaces

# Create the series of countries: countries
countries = gapminder['country']

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~countries.str.contains(pattern)

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)