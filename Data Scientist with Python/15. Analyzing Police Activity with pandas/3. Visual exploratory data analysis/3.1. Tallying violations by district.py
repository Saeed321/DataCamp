# Tallying violations by district

# The state of Rhode Island is broken into six police districts, also known as zones. How do the zones compare in terms of what violations are caught by police?
# In this exercise, you'll create a frequency table to determine how many violations of each type took place in each of the six zones. Then, you'll filter the table to focus on the "K" zones, which you'll examine further in the next exercise.

# Instructions

# �	Create a frequency table from the district and violation columns using the pd.crosstab() function.
# �	Save the frequency table as a new object, all_zones.
# �	Select rows 'Zone K1' through 'Zone K3' from all_zones using the .loc[] accessor.
# �	Save the smaller table as a new object, k_zones

# Create a frequency table of districts and violations
print(pd.crosstab(ri.district, ri.violation))

# Save the frequency table as 'all_zones'
all_zones = pd.crosstab(ri.district, ri.violation)

# Select rows 'Zone K1' through 'Zone K3'
print(all_zones.loc['Zone K1':'Zone K3'])

# Save the smaller table as 'k_zones'
k_zones = all_zones.loc['Zone K1':'Zone K3']