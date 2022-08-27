
#	Inside the f-string, access the values of the keys price and date in east dictionary. Format the date to month-day-year.

Hint

#	To access a value of key in dict inside a f-string, use f"{dict['key']}". To format the date, use the specifiers %m, %d and %Y.

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

#	Inside the f-string, access the values of the keys price and date in west dictionary. Format the date to month-day-year.

Hint

#	To access a value of key in dict inside a f-string, use f"{dict['key']}". To format the date, use the specifiers %m, %d and %Y.

# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")
