# Indexing multiple levels of a MultiIndex

# Looking up indexed data is fast and efficient. And you have already seen that lookups based on the outermost level of a MultiIndex work just like lookups on DataFrames that have a single-level Index.
# Looking up data based on inner levels of a MultiIndex can be a bit trickier. The trickiest of all these lookups are when you want to access some inner levels of the index. In this case, you need to use slice(None) in the slicing parameter for the outermost dimension(s) instead of the usual :, or use pd.IndexSlice. You can refer to the pandas documentation for more details. For example, in the video, Dhavide used the following code to extract rows from all Symbols for the dates Oct. 3rd through 4th inclusive:
# stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]
# Pay particular attention to the tuple (slice(None), slice('2016-10-03', '2016-10-04')).
# In this exercise, you will use your sales DataFrame to do some increasingly complex lookups. Remember that you can type sales.head() in the console to review the structure of the DataFrame!

# Instructions

# �	Look up data for New York ('NY') in month 1 in the salesDataFrame.
# �	Look up data for California and Texas ('CA', 'TX') in month 2.
# �	Access the inner index month and look up data for all states in month 2. Use (slice(None), 2) to extract all rows in month 2.

# Look up data for NY in month 1 in sales: NY_month1
NY_month1 = sales.loc['NY',1]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2),:]

# Access the inner month index and look up data for all states in month 2: all_month2
all_month2 = sales.loc[(['CA','NY','TX'], 2),:]