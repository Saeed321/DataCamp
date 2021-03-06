# Iterating with .itertuples()

# Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple. You can look up an attribute within a namedtuple with a special syntax. Let's practice working with namedtuples.
# A pandas DataFrame has been loaded into your session called rangers_df. This DataFrame contains the stats ('Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', and 'Playoffs') for the Major League baseball team named the Texas Rangers (abbreviated as 'TEX').

# Use .itertuples() to loop over rangers_df and print each row.

# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)

# Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins.

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  print(i, year, wins)

# Now, loop over rangers_df and print these values only for those rowswhere the Rangers made the playoffs.

  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1 == 1:
    print(i, year, wins)