# Characterizing the network (II)

# Let's continue recalling what you've learned before about node importances, by plotting the degree distribution of a network. This is the distribution of node degrees computed across all nodes in a network.

# Instructions

# •	Plot the degree distribution of the GitHub collaboration network G. Recall that there are four steps involved here:
# o	Calculating the degree centrality of G.
# o	Using the .values() method of G and converting it into a list.
# o	Passing the list of degree distributions to plt.hist().
# o	Displaying the histogram with plt.show().

# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.degree_centrality(G).values()))
plt.show()