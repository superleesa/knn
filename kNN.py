import numpy as np
from math import sqrt
import pandas as pd
import random
from typing import Union

class kNearestNeighbor:
    def __init__(self, X_example_data: np.array, X_input_data: np.array, y_example_data: np.array, k, classification=None) -> None:
        self.X_example_data = X_example_data
        self.X_input_data = X_input_data
        self.y_example_data = y_example_data

        self.k = k

        if classification is None:
            self.classification = self._decide_classification_or_regression()
        else:
            self.classification = classification

        self.result = None

    def _eucledian_distance(self, query: np.array, example_data_point: np.array) -> int:
        # need to exclude the target
        # does not do apply the square root but the result still the same
        return sum((query-example_data_point)**2)

    def _decide_classification_or_regression(self) -> bool:
        # implemented using hash table (a dictionary)

        labels = {}
        # traverse through the labels and find the number of classes
        for label in self.y_example_data:
            try:
                labels[str(label)]
            except KeyError:
                labels[str(label)] = True
                if len(labels) > 10:
                    return False

        return True

    def _find_label_type(self):
        return self.y_example_data.dtype

    def _find_mode_class(self, sorted_example_data: np.array):
        # if more than one class have the same appearances -> choice is arbitary

        classes = {}

        for i in range(self.k):
            current_label = sorted_example_data[i, 1]
            try:
                classes[str(current_label)][1] += 1

            except KeyError:
                classes[str(current_label)] = [current_label, 1]

        mode = -1
        mode_class = None
        for key in classes:
            appearances = classes[key][1]
            if appearances > mode:
                mode = appearances
                mode_class = classes[key][0]

        return mode_class


    def _average_labels(self, sorted_learning_data: np.array):
        total = 0
        for i in range(self.k):
            total += sorted_learning_data[self.k, 1]

        return total / self.k

    def predict(self) -> np.array:
        """
        - a brute force algorithm to predict some unseen data
        - both example data must be split into features and labels
        - uses Euclidean distance as the distance measure
        - uses numpy (not Python built-in list)

        :param X_example_data:
        :param X_input_data:
        :param y_example_data:
        :return: numpy array
        """

        # sorts the whole data based on the distance to the query
        results = np.zeros(len(self.X_input_data), dtype=self._find_label_type())
        for input_data_idx in range(len(self.X_input_data)):

            distances = np.zeros((len(self.X_example_data), 2))
            for example_data_idx in range(len(self.X_example_data)):
                distance = self._eucledian_distance(self.X_example_data[example_data_idx], self.X_input_data[input_data_idx])
                distances[example_data_idx, 0] = distance
                distances[example_data_idx, 1] = self.y_example_data[example_data_idx]

            sorted_example_data_labels = distances[distances[:, 0].argsort()]

            if self.classification:
                results[input_data_idx] = self._find_mode_class(sorted_example_data_labels)
            else:
                # regression
                results[input_data_idx] = self._average_labels(sorted_example_data_labels)

        self.result = results
        return results

    def compare_with_actual_labels(self, y_input_data: np.array):
        """
        returns accuracy if self.classification is True; else, returns the RMSE
        :return:
        """

        if self.classification:
            return np.sum(y_input_data == self.result) / len(y_input_data)
        else:
            return np.sqrt(np.mean((self.result - y_input_data)**2))

def kNN_kd_tree():
    #TODO
    pass


if __name__ == "__main__":
    X_example_data = np.array([
        [1, 3],
        [10, 9],
        [2, 5],
        [9, 10],
        [8.5, 9],
        [2, 4],
        [11, 11]
    ])
    y_example_data = np.array([0, 1, 0, 1, 1, 0, 1])

    X_input_data = np.array([[10, 10], [1.7, 4.3]])
    y_input_data = np.array([1, 0])

    knn = kNearestNeighbor(X_example_data, X_input_data, y_example_data, 3, classification=True)
    res = knn.predict()

    print(res)
    print(y_input_data == res)
    print(knn.compare_with_actual_labels(y_input_data))