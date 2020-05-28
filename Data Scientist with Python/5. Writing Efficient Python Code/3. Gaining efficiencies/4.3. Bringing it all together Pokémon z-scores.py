# Bringing it all together: Pok�mon z-scores

# A list of 720 Pok�mon has been loaded into your session as names. Each Pok�mon's corresponding Health Points is stored in a NumPy array called hps. You want to analyze the Health Points using the z-score to see how many standard deviations each Pok�mon's HP is from the mean of all HPs.
# The below code was written to calculate the HP z-score for each Pok�mon and gather the Pok�mon with the highest HPs based on their z-scores:
# poke_zscores = []
# 
# for name,hp in zip(names, hps):
#     hp_avg = hps.mean()
#     hp_std = hps.std()
#     z_score = (hp - hp_avg)/hp_std
#     poke_zscores.append((name, hp, z_score))
# high_hp_pokemon = []
# 
# for name,hp,zscore in poke_zscores:
#     if zscore > 2:
#         high_hp_pokemon.append((name, hp, zscore))

# �	Use NumPy to eliminate the for loop used to create the z-scores.
# �	Then, combine the names, hps, and z_scores objects together into a list called poke_zscores2.

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')


# �	Use list comprehension to replace the for loop used to collect Pok�mon with the highest HPs based on their z-score.

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon = [(name, hp, zscore) for name,hp,zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon, sep='\n')

# Use %%timeit (cell magic mode) within your IPython console to compare the runtimes between the original code blocks and the new code you developed using NumPy and list comprehension.
# Don't include the print() statements when timing. You should include ten lines of code when timing the original code blocks and five lines of code when timing the new code you developed. You may need to press SHIFT+ENTERafter entering %%timeit to get to a new line within your IPython console.
# Which approach was the faster?
# Possible Answers

# The total time for executing both of the original code blocks was faster.

# The total time for executing the updated solution using NumPy and list comprehension was faster.

# Both approaches had the same execution time.

# Answer : The total time for executing the updated solution using NumPy and list comprehension was faster.