# Custom kNN

This repository implements a kNearstNeighbor algorithm from scratch, using Numpy only.

There are two implementations of the kNN algorithm:
1. Naive kNN, calculating the Euclidean distance from the test data point to all example datasets, choosing the k-closest neighbors, and returning the average of those neighbors.
2. kNN using KD-Tree. We put all the example data points into a data structure called KD-Tree first and then used the brunch and bound technique to find the closest points quickly. (This implementation is still progressing.)
