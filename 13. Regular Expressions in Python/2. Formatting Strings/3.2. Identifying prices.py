
#	Assign the first, second, and third element of tools to the variables our_tool, our_fee and our_pay respectively.
#	Complete the template string using $tool, $fee, and $pay as identifiers. Add the dollar sign before the $fee identifier and add the characters ly directly after the $pay identifier.
#	Substitute identifiers with the three variables you created and print out the results.

Hint

#	To select the nth element of list, use list[n-1].
#	To write a template, use Template("$identifier1 text $indentifier2"). Remember you need to escape the dollar sign by using $$ and use ${identifier} to add valid characters immediately after.
#	To substitute an $identifier in a tempstr with a value, use tempstr.substitute(identifier=value).

# Import template
from string import Template

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))
