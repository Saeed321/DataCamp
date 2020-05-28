# Gathering unique Pok�mon

# A sample of 500 Pok�mon has been created with replacement (meaning a Pok�mon could be selected more than once and duplicates exist within the sample).
# Three lists have been loaded into your session:
# �	The names list contains the names of each Pok�mon in the sample.
# �	The primary_types list containing the corresponding primary type of each Pok�mon in the sample.
# �	The generations list contains the corresponding generation of each Pok�mon in the sample.

# The below function was written to gather unique values from each list:
def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques

# Let's compare the above function to using the set data type for collecting unique items.

# 1. �	Use the provided function to collect the unique Pok�mon in the nameslist. Save this as uniq_names_func.

# Use the provided function to collect unique Pok�mon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# 2. �	Use a set data type to collect the unique Pok�mon in the names list. Save this as uniq_names_set.

# Convert the names list to a set to collect unique Pok�mon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Within your IPython console, use %timeit to compare the find_unique_items() function with using a set data type to collect unique Pok�mon character names in names.
# Which membership testing was faster?

# Possible Answers

# Using a set to collect unique values is faster.

# Using the provided function that uses a loop to gather unique items is faster.

# Both approaches have the same runtime.

# Answer : Using a set to collect unique values is faster.

# 3. �	Use the most efficient approach for gathering unique items to collect the unique Pok�mon types (from the primary_types list) and Pok�mon generations (from the generations list).

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n')