
#	Inside the f-string, include number1,number2 and the result of dividing number1 by number2 rounded to one decimal.

Hint

#	To perform an operation between var1 and var2 inside a f-string, use f"{var1 * var2}". Remember that you can use the format specifier :.nf to indicate the number n of decimals.

# Include both variables and the result of dividing them 
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2:.1f} tweets per min")

#	Inside the f-string, use .replace() to replace the substring https with an empty substring in string1.

Hint

#	To call the function .replace() on my_string inside a f-string, use f"text {my_string.replace()}". Remember escape sequences are not allowed; different quotes need to be used for the f-string and the strings inside .replace().

# Replace the substring http by an empty string
print(f"{string1.replace('https', '')}")

#	Inside the f-string, get list_links length, multiply it by 100 and divide it by 120. Round the result to two decimals.

Hint

#	To get the length of my_list inside an f-string, use the syntax f"text {len(my_list)}". Remember that you can use the format specifier :.nf to indicate the number n of decimals.

# Divide the length of list by 120 rounded to two decimals
print(f"Only {(len(list_links)*100/120):.2f}% of the posts contain links")
