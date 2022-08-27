
#	Complete the for-loop with a regex that finds all dates in a format similar to 27 minutes ago or 4 hours ago.

Hint

#	To match a number that appears once or twice, use \d{1,2}. Remember that \s indicates whitespace present in the pattern. You can use \w for normal characters together with + to specify that it can be repeated once or more times. Pay attention that both formats end in ago and normal characters match themselves. To find all matches use .findall().

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\s\w+\sago", date))

#	Complete the for-loop with a regex that finds all dates in a format similar to 23rd june 2018.

Hint

#	To match a number that appears once or twice, use \d{1,2}. Remember that \s indicates whitespace present in the pattern. You can use \w for normal characters together with + to specify that it can be repeated once or more times. If a date ends with the year you can use the {n} quantifier to specify that the number is repeated exactly n times. To find all matches use .findall().

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))

#	Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25.

Hint

#	To specify the time, you can use \d together with the {n,m} quantifier to indicate a minimum n and a maximum m numbers of times. The : is there to match the : appearing between numbers. Remember that \sindicates whitespace present in the pattern. To find all matches use .findall().

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))
