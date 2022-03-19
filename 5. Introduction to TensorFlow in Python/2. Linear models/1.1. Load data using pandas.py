•	Import pandas under the alias pd.
•	Assign the path to a string variable with the name data_path.
•	Load the dataset as a pandas dataframe named housing.
•	Print the price column of housing.

# Import pandas under the alias pd
import pandas as pd

# Assign the path to a string variable named data_path
data_path = 'kc_house_data.csv'

# Load the dataset as a dataframe named housing
housing = pd.read_csv(data_path)

# Print the price column of housing
print(housing['price'])
