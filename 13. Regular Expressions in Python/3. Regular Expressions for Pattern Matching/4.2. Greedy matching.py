
#	Use a lazy quantifier to match all numbers that appear in the variable sentiment_analysis.

Hint

#	In order to use a lazy quantifier, append ? to a regex that looks for numbers that occur one or more times. Don't forget to use .findall()method from the re module.

# Write a lazy regex expression 
numbers_found_lazy = re.findall(r"[0-9]+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

#	Now, use a greedy quantifier to match all numbers that appear in the variable sentiment_analysis.

Hint

#	In order to use a greedy quantifier, write a regex that looks for numbers that appear once or multiple times. Don't forget to use .findall() method from the re module.


# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"[0-9]+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)
