import random

def train_test_split(X: np.array, y: np.array, ratio: int, seed=None):
    # ratio must be smaller than 1, bigger than 0
    # return error if n == 0

    # returns (train_features, train_labels), (test_features, test_labels)

    n = int(ratio * len(X))
    if n < 1:
        raise ValueError("ratio too small compared to the data size (cannot split)")

    # selecting random indices
    if seed:
        random.seed(seed)
    indices = random.sample(range(0, len(X)), n)

    # mark the selected indices
    marks = [False] * (len(X))
    for idx in indices:
        marks[idx] = True

    # select items specified by marks
    X_train_data, X_test_data = np.array([]), np.array([])
    y_train_data, y_test_data = np.array([]), np.array([])

    for idx in range(len(marks)):
        if marks[idx]:
            X_train_data = np.append(X[idx], X_train_data)
            y_train_data = np.append(y[idx], y_train_data)
        else:
            X_test_data = np.append(X[idx], X_test_data)
            y_test_data = np.append(y[idx], y_test_data)

    return X_train_data, X_test_data, y_train_data, y_test_data