# Comparing Pok�dexes
# Two Pok�mon trainers, Ash and Misty, would like to compare their individual collections of Pok�mon. Let's see what Pok�mon they have in common and what Pok�mon Ash has that Misty does not.
# Both Ash and Misty's Pok�dex (their collection of Pok�mon) have been loaded into your session as lists called ash_pokedex and misty_pokedex. They have been printed into the console for your convenience.

# Instructions

# �	Convert both lists (ash_pokedex and misty_pokedex) to sets called ash_set and misty_set respectively.
# �	Find the Pok�mon that both Ash and Misty have in common using a set method.
# �	Find the Pok�mon that are within Ash's Pok�dex but are not within Misty's Pok�dex with a set method.
# �	Use a set method to find the Pok�mon that are unique to either Ash or Misty (i.e., the Pok�mon that exist in exactly one of the Pok�dexes but not both).

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pok�mon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pok�mon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pok�mon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)