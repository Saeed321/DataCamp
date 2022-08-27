
#	Get all cell phones numbers that are not preceded by the optional area code.

Hint

#	To get all matches of a pattern that are not preceded by a subpattern, use (?<!subpattern)pattern. Remember to use \d for digits. Use {n, m} to specify a minimum of n and a maximum of m repetitions.
for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)

#	Get all the cell phones numbers that are not followed by the optional extension.

Hint

#	To get all matches of a pattern that are not followed by a subpattern, use pattern(?!subpattern). Remember to use \d for digits. Use {n, m} to specify a minimum of n and a maximum of m repetitions.
for phone in cellphones:
	# Get all phone numbers not followed by optional extension
	number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number)
