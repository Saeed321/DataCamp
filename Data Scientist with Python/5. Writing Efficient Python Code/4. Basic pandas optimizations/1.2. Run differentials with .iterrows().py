# Run differentials with .iterrows()
# You've been hired by the San Francisco Giants as an analyst—congrats! The team's owner wants you to calculate a metric called the run differential for each season from the year 2008 to 2012. This metric is calculated by subtracting the total number of runs a team allowed in a season from the team's total number of runs scored in a season. 'RS' means runs scored and 'RA' means runs allowed.

# The below function calculates this metric:
def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

# A DataFrame has been loaded into your session as giants_df and printed into the console. Let's practice using .iterrows() to add a run differentialcolumn to this DataFrame.

# •	Create an empty list called run_diffs that will be used to store the run differentials you will calculate.
# Create an empty list to store run differentials
run_diffs = ()

# •	Write a for loop that uses .iterrows() to loop over giants_df and collects each row's runs scored and runs allowed.

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row[3]
    runs_allowed = row[4]

# •	Add a line to the for loop that uses the provided function to calculate each row's run differential.

# Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)

# •	Add a line to the loop that appends each row's run differential to the run_diffs list.

# Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)