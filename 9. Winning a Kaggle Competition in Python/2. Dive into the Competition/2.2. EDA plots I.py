•	Create a new variable "distance_km" as Haversine distance between pickup and dropoff points.
•	Plot a scatterplot with "fare_amount" on the x axis and "distance_km" on the y axis. To draw a scatterplot use matplotlib scatter() method.
•	Set a limit on a ride distance to be between 0 and 50 kilometers to avoid plotting outliers.

# Calculate the ride distance
train['distance_km'] = haversine_distance(train)

# Draw a scatterplot
plt.scatter(x=train['fare_amount'], y=train['distance_km'], alpha=0.5)
plt.xlabel('Fare amount')
plt.ylabel('Distance, km')
plt.title('Fare amount based on the distance')

# Limit on the distance
plt.ylim(0, 50)
plt.show()
