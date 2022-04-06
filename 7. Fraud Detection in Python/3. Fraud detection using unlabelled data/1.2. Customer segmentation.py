•	Group the dataframe df by the age category age and get the means for each age group.
# Group by age groups and get the mean
print(df.groupby('age').mean())

•	Count the values of each age group.
# Group by age groups and get the mean
df.groupby('age').mean()

# Count the values of the observations in each age group
print(df['age'].value_counts())

Question

Based on the results you see, does it make sense to divide your data into age segments before running a fraud detection algorithm?

Possible Answers
	 
No, the age groups who are the largest are relatively similar.
	 
Yes, the age group "0" is very different and I would split that one out.

Answer : No, the age groups who are the largest are relatively similar.
