#	Specify the grids for possible max_depth and subsample values. For max_depth: 3, 5 and 7. For subsample: 0.8, 0.9 and 1.0.
#	Apply the product() function from the itertools package to the hyperparameter grids. It returns all possible combinations for these two grids.
#	Pass each hyperparameters candidate couple to the model paramsdictionary.

import itertools

# Hyperparameter grids
max_depth_grid = [3, 5, 7]
subsample_grid = [0.8, 0.9, 1.0]
results = {}

# For each couple in the grid
for max_depth_candidate, subsample_candidate in itertools.product(max_depth_grid, subsample_grid):
    params = {'max_depth': max_depth_candidate,
              'subsample': subsample_candidate}
    validation_score = get_cv_score(train, params)
    # Save the results for each couple
    results[(max_depth_candidate, subsample_candidate)] = validation_score   
print(results)
