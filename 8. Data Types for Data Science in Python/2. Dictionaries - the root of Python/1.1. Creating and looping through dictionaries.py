•	Create an empty dictionary called names_by_rank.
•	Loop over female_baby_names_2012.items(), unpacking it into the variables rank and name.
•	Inside the loop, add each name to the names_by_rank dictionary using the rank as the key.
•	Sort the names_by_rank dictionary keys in descending order, select the first ten items. Print each item.

# Create an empty dictionary: names_by_rank
names_by_rank = dict()

# Loop over the girl names
for rank, name in female_baby_names_2012.items():
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name
    
# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for rank in sorted(names_by_rank, reverse=True)[:10]:
    # Print each item
    print(names_by_rank[rank])
