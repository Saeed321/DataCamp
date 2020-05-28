# Combinations of Pok�mon
# Ash, a Pok�mon trainer, encounters a group of five Pok�mon. These Pok�mon have been loaded into a list within your session (called pokemon) and printed into the console for your convenience.
# Ash would like to try to catch some of these Pok�mon, but his Pok�dex can only store two Pok�mon at a time. Let's use combinations from the itertools module to see what the possible pairs of Pok�mon are that Ash could catch.

# Instructions

# �	Import combinations from itertools.
# �	Create a combinations object called combos_obj that contains all possible pairs of Pok�mon from the pokemon list. A pair has 2 Pok�mon.
# �	Unpack combos_obj into a list called combos_2.
# �	Ash upgraded his Pok�dex so that it can now store four Pok�mon. Use combinations to collect all possible combinations of 4 different Pok�mon. Save these combinations directly into a list called combos_4using the star character (*).

# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pok�mon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pok�mon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)