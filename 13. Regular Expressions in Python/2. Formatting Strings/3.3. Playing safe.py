
#	Complete the template string using $answer1 and $answer2 as identifiers.

Hint

#	To create a template string, use the following syntax: Template("text $identifier text2 $identifier2").

# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

#	Use the method .substitute() to replace the identifiers with the values in answers in the predefined template.

Hint

#	To substitute identifiers in a tempstr by values in a dict, use tempstr.substitute(dict). Remember that if any placeholder is missing, it will raise an error.

# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use substitute to replace identifiers
try:
    print(the_answers.substitute(answers))
except KeyError:
    print("Missing information")

#	Use the method .safe_substitute() to replace the identifiers with the values in answers in the predefined template.

Hint

#	To safe substitute identifiers in a tempstr by values in a dict, use tempstr.safe_substitute(dict). If any placeholder is missing, the original placeholder will be used by default.

# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")
