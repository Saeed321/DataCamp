
#	Write a regex that captures the month, day, and year in which the contract was signed. Scan contract for matches.

Hint

#	To capture a group, place the expression inside parentheses (group). To find a number repeated m times you can use {m} quantifier. The \smatches the spaces between the words. Don't forget to match the words signed, on before the date. Use .search() to scan the string for a match.

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

#	Assign each captured group to the corresponding keys in the dictionary.

Hint

#	To retrieve captured groups, you can use the numbers assigned to them in the matching process. The m group match can be retrieved using .group(m). Remember that the first matched group receives the number 1.

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}

#	Complete the positional method to print out the captured groups. Use the values corresponding to each key in the dictionary.

Hint

#	To insert values associated with a key in a dictionary, remember the .format() syntax: text {data[key]}".format(data=dictionary).

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}
# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))
