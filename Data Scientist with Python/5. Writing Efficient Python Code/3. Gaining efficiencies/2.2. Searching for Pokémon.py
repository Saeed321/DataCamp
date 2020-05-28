# Searching for Pok�mon
# Two Pok�mon trainers, Ash and Brock, have a collection of ten Pok�mon each. Each trainer's Pok�dex (their collection of Pok�mon) has been loaded into your session as lists called ash_pokedex and brock_pokedex respectively.
# You'd like to see if certain Pok�mon are members of either Ash or Brock's Pok�dex.
# Let's compare using a set versus using a list when performing this membership testing.

# 1. �	Convert Brock's Pok�dex list (brock_pokedex) to a set called brock_pokedex_set.

# Convert Brock's Pok�dex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# 2. �	Check if 'Psyduck' is in Ash's Pok�dex list (ash_pokedex) and if 'Psyduck' is in Brock's Pok�dex set (brock_pokedex_set).

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# 3. �	Check if 'Machop' is in Ash's Pok�dex list (ash_pokedex) and if 'Machop' is in Brock's Pok�dex set (brock_pokedex_set).

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

# Question
# Within your IPython console, use %timeit to compare membership testing for 'Psyduck' and for 'Machop' in ash_pokedex and brock_pokedex_set (a total of four different timings).
# Don't include the print() function. Only time the commands that you wrote inside the print() function in the previous steps.
# Which membership testing was faster?

# Possible Answers

# Using a list is faster than using a set for membership testing in all four cases.

# Member testing using a list and a set have the same runtimes for all four cases.

# Member testing using a set is faster than using a list in all four cases.

# Answer : Member testing using a set is faster than using a list in all four cases.