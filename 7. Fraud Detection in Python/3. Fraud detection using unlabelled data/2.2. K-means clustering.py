•	Import MiniBatchKMeans from sklearn.
•	Initialize the minibatch kmeans model with 8 clusters.
•	Fit the model to your scaled data.

# Import MiniBatchKmeans 
from sklearn.cluster import MiniBatchKMeans

# Define the model 
kmeans = MiniBatchKMeans(n_clusters=8, random_state=0)

# Fit the model to the scaled data
kmeans.fit(X_scaled)
