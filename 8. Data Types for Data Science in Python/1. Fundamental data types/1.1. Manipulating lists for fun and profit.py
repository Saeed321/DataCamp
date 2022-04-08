•	Create a list called baby_names with the names 'Ximena', 'Aliza', 'Ayden', and 'Calvin'.
•	Use the .extend() method on baby_names to add 'Rowen' and 'Sandeep' and print the list.
•	Use the .index() method to find the position of 'Aliza' in the list. Save the result as position.
•	Use the .pop() method with position to remove 'Aliza' from the list.
•	Print the baby_names list. This has been done for you, so hit 'Submit Answer' to see the results!

# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(['Rowen', 'Sandeep'])

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index('Aliza')

# Remove 'Aliza' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)
