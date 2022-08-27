
#	Find the index where money occurs between characters with index 12 and 50. If not found, the method should return -1.

Hint

#	To find the first occurrence of pattern in string between characters with index 1 and 5 and return -1 if not found, use string.find(pattern, 1, 6). Remember that the ending position is exclusive.
for movie in movies:

  # Find the first occurrence of word
  print(movie.find("money", 12, 51))

#	Find the index where money occurs between characters with index 12 and 50. If not found, it should raise an error.

Hint

#	To find the first occurrence of pattern in string between characters with index 1 and 5 and raise and error if not found, use string.index(pattern, 1, 6). Remember that the ending position is exclusive.
for movie in movies:

  try:
    # Find the first occurrence of word
  	print(movie.index("money", 12, 51))
  except ValueError:
    print("substring not found")
