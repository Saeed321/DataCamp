
#	Complete the f-string to include the variable field1 with quotes and the variable fact1 as a digit.

Hint

#	For an f-string, use the syntax f"string {variable}". After the variable inside the expression, use the type !r to convert to string and show the quotes, and :d for specifying digits.

# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1:d}st century")

#	Complete the f-string to include the the variable fact2 using exponential notation, and the variable field2.

Hint

#	For f-string, use the syntax f"string {variable}". After the variable inside the expression use :e for specifying that you want exponential notation.

# Complete the f-string
print(f"About {fact2:e} of {field2} in the world")

#	Complete the f-string to include field3 together with fact3 rounded to 2 decimals, and fact4 rounded to one decimal.

Hint

#	For f-string, use the syntax f"string {variable}". For specifying number of n decimals in a float, use :.nf after the variable inside the expression.
# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")
