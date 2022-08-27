
#	Import the function datetime from the module datetime .
#	Obtain the date of today and assign it to the variable get_date.
#	Complete the string message by adding placeholders named today and the format specifiers to format the date as month_name day, year and time as hour:minutes.
#	Print the message using the .format() method and the variable get_date to replace the named placeholders.

Hint

#	Use: from module import function.
#	Remember that you can use the function datetime to access .now()and obtain today's date.
#	Add a name to a placeholder using text {name}. Format date using %B %d, %Y and time %H:%M.
#	To replace a named placeholder with a value in my_string, use my_string.format(named=value).

# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Format date
print(message.format(today=get_date))
