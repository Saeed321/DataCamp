•	Import pandas as pd.
•	Read train data using pandas' read_csv() method.
•	Print the head of the train data (using head() method) to see the data sample.

# Import pandas
import pandas as pd

# Read train data
train = pd.read_csv('train.csv')

# Look at the shape of the data
print('Train shape:', train.shape)

# Look at the head() of the data
print(train.head())
