
#	Use a greedy quantifier to match text that appears within parentheses in the variable sentiment_analysis.

Hint

#	For a greedy approach, use the quantifier .*. Remember to use \ to escape the parentheses. Use .findall() method to find all matches.

# Write a greedy regex expression to match 
sentences_found_greedy = re.findall(r"\(.*\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

#	Now, use a lazy quantifier to match text that appears within parentheses in the variable sentiment_analysis.

Hint

#	For the lazy mode, append ? to the quantifier .*. Remember to use \to escape the parenthesis. Use .findall() method to find all matches.

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)
