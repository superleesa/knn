import numpy as np
from MaxHeap import MaxHeap
from Timsort import range_sort_points_by_axis

class Node:
    def __init__(self):
        self.coordinate = None
        self.left : Node = None
        self.right : Node = None
        self.depth = 0  # TODO alter this value during construction
        self.distance_to_query = None

class KD_TREE:
    #TODO

    def __init__(self, pointlist: list):
        self.pointlist = []
        self.dimension = len(pointlist[0])  # all data points must have the same dimensions
        self.root = None
        self.maxheap = MaxHeap()

        self.construct()

    def construct(self) -> None:
        # find root node first
        # sort list and find the median element
        # range_sort_points_by_axis(self.pointlist, 0, 0, len(self.pointlist))
        # median_idx = (len(self.pointlist)-1 + 1) // 2
        # self.root = self.pointlist[median_idx]

        self.construct_aux(0, len(self.pointlist), 0, self.root)


    def construct_aux(self, lower, upper, depth, current: Node):
        # lower inclusive; upper exclusive
        # TODO if does not work change the upper to be inclusive

        # recursive algorithm

        if lower == upper:
            return None

        else:
            # select axis
            axis = depth % self.dimension

            # sort the pointlist based on axis
            range_sort_points_by_axis(self.pointlist, axis, lower, upper)
            median_idx = (upper+lower)//2

            # set data point coordinate
            current.coordinate = self.pointlist[median_idx]

            # set left subtree
            print("passes here")
            print(lower, median_idx)
            current.left = self.construct_aux(lower, median_idx, depth+1, current)
            # set right subtree
            current.right = self.construct_aux(median_idx+1, upper, depth+1, current)

            return current


    def kNN(self):
        pass


    def euclidean_distance(self, X: np.array, Y: np.array):
        return sum((X - Y)**2)

    # def kNN_aux(query, current, depth, k):
    #     # the parameter k here doesn't represent dimentionality but k neighbors
    #     # start
    #     # base case
    #     if current is None:
    #         return
    #
    #     else:
    #         current_axis = depth % self.k
    #         if query[current_axis] > current.coordinate[current_axis]:
    #             res = self.kNN_aux(query, current.right, depth+1, k)
    #         elif query[current_axis] < current.coordinate[current_axis]:
    #             res = self.kNN_aux(query, current.left, depth+1, k)
    #         else:
    #             pass
    #
    #         if res is not None:
    #
    #             pass
    #         else:
    #             # res is None -> need to calculate current best
    #             current_best = self.euclidean_distance(current.coordinate[current_axis], query)
    #             return current_best

    def knn_aux(self, query, current: Node, k):
        # this algorithm assumes that the tree is balanced

        # base case - left or right subtree doesn't exist
        # TODO edge case: there might be no element in the heap yet
        if current.left is None and current.right is not None:
            distance_right_node_to_query = self.euclidean_distance(current.right.coordinate, query)
            current_farthest = self.maxheap.peakmax()
            if current_farthest > distance_right_node_to_query:
                self.maxheap.getmax()
                self.maxheap.put(distance_right_node_to_query)

        elif current.left is not None and current.right is None:
            distance_left_node_to_query = self.euclidean_distance(current.left.coordinate, query)
            current_farthest = self.maxheap.peakmax()
            if current_farthest > distance_left_node_to_query:
                self.maxheap.getmax()
                self.maxheap.put(distance_left_node_to_query)

        else:

            # recursive case - at a particular node
            current_axis = current.depth % self.dimension
            distance_current = self.euclidean_distance(current.coordinate, query)
            current_farthest = self.maxheap.peakmax()
            if distance_current < current_farthest:
                self.maxheap.getmax()
                self.maxheap.put(distance_current)

            # compare two childs
            distance_left_child_this_axis = abs(current.left.coordinate[current_axis] - query[current_axis])
            distance_right_child_this_axis = abs(current.right.coordinate[current_axis] - query[current_axis])

            if distance_left_child_this_axis >= distance_right_child_this_axis:
                self.knn_aux(query, current.left, k)

                # be careful with equal sign here
                current_farthest = self.maxheap.peakmax()
                if distance_right_child_this_axis <= current_farthest:
                    self.knn_aux(query, current.right, k)

            else:
                self.knn_aux(query, current.right, k)

                # be careful with equal sign here
                current_farthest = self.maxheap.peakmax()
                if distance_right_child_this_axis <= current_farthest:
                    current_best = self.knn_aux(query, current.left, k)

    def visualize(self):
        self.find_max_depth()

    def find_max_depth(self):

        current = self.root
        max_depth = 0
        while current is not None:
            max_depth = current