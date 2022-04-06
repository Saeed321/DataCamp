•	Define the range to be between 1 and 10 clusters.
•	Run MiniBatch K-means on all the clusters in the range using list comprehension.
•	Fit each model on the scaled data and obtain the scores from the scaled data.
•	Plot the cluster numbers and their respective scores.

# Define the range of clusters to try
clustno = range(1, 10)

# Run MiniBatch Kmeans over the number of clusters
kmeans = [MiniBatchKMeans(n_clusters=i) for i in clustno]

# Obtain the score for each model
score = [kmeans[i].fit(X_scaled).score(X_scaled) for i in range(len(kmeans))]

# Plot the models and their respective score 
plt.plot(clustno, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()
