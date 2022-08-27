
#	Get all the words that are followed by the word python in sentiment_analysis. Print out the word found.

Hint

#	In order to indicate that you want what comes before word, use (?=\sword). You can use \w to indicate word characters. Use the findall function of the re module.

# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

#	Get all the words that are preceded by the word python or Python in sentiment_analysis. Print out the words found.

Hint

#	In order to find words that are preceded by word or Word, use the findall() function of the re module and the regex expression (?<=[Ww]ord\s). Indicate word characters using \w.

# Positive lookbehind
look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)
