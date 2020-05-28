# Using %timeit: your turn!
# You'd like to create a list of integers from 0 to 50 using the range() function. However, you are unsure whether using list comprehension or unpacking the range object into a list is faster. Let's use %timeit to find the best implementation.
# For your convenience, a reference table of time orders of magnitude is provided below (faster at the top).
# symbol	name	unit (s)
# ns	nanosecond	10-9
# µs (us)	microsecond	10-6
# ms	millisecond	10-3
# s	second	100

# Instructions

# 1. •	Use list comprehension and range() to create a list of integers from 0 to 50 called nums_list_comp.
# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(0, 51)]
print(nums_list_comp)

# 2. •	Use range() to create a list of integers from 0 to 50 and unpack its contents into a list called nums_unpack.
# Create a list of integers (0-50) by unpacking range
nums_unpack = [range(51)]
print(nums_unpack)

# 3. Use %timeit within your IPython console to compare the runtimes for creating a list of integers from 0 to 50 using list comprehension vs. unpacking the range object. Don't include the print() statements when timing.

# Which method was faster?
# Possible Answers

# List comprehension was faster than unpacking range().

# Unpacking the range object was faster than list comprehension.

# Both methods had the same runtime.

# Answer : List comprehension was faster than unpacking range().