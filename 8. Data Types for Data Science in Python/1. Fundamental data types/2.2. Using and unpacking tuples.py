•	Use the zip() function to pair up girl_names and boy_names into a variable called pairs.
•	Use a for loop to loop through pairs, using enumerate() to keep track of your position. Unpack pairs into the variables idx and pair.
•	Inside the for loop:
•	Unpack pair into the variables girl_name and boy_name.
•	Print the rank, girl name, and boy name, in that order. The rank is contained in idx.


# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))
