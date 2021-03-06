# Iterating and concatenating all matches

# Now that you have a list of filenames to load, you can load all the files into a list of DataFrames that can then be concatenated.
# You'll start with an empty list called frames. Your job is to use a for loop to:
# 1.	iterate through each of the filenames
# 2.	read each filename into a DataFrame, and then
# 3.	append it to the frames list.
# You can then concatenate this list of DataFrames using pd.concat(). Go for it!

# Instructions

# �	Write a for loop to iterate through csv_files:
# o	In each iteration of the loop, read csv into a DataFrame called df.
# o	After creating df, append it to the list frames using the .append()method.
# �	Concatenate frames into a single DataFrame called uber.

# �	Hit 'Submit Answer' to see the head and shape of the concatenated DataFrame!

# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())