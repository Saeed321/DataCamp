# Many-to-many data merge

# The final merging scenario occurs when both DataFrames do not have unique keys for a merge. What happens here is that for each duplicated key, every pairwise combination will be created.
# Two example DataFrames that share common key values have been pre-loaded: df1 and df2. Another DataFrame df3, which is the result of df1 merged with df2, has been pre-loaded. All three DataFrames have been printed - look at the output and notice how pairwise combinations have been created. This example is to help you develop your intuition for many-to-many merges.
# Here, you'll work with the site and visited DataFrames from before, and a new survey DataFrame. Your task is to merge site and visitedas you did in the earlier exercises. You will then merge this merged DataFrame with survey.
# The survey, visited, and site DataFrames are available.

# Instructions

# Merge survey, visited, and site to get a single data frame, m2m. Each row should represent a survey, but also contain the details of the corresponding visit, and the details of the site associated with that visit. Print m2m.
# Merge survey, visited and site to a single data frame
# of surveys with visit and site details

# Merge the DataFrames: m2o
m2o = pd.merge(left = survey, right = visited, left_on = "taken", right_on = "ident")
m2m = pd.merge(left = m2o, right = site, left_on = 'site', right_on ='name')
print(m2m)