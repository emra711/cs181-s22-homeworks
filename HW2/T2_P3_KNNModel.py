from unittest.util import sorted_list_difference
import numpy as np

# Please implement the predict() method of this class
# You can add additional private methods by beginning them with
# two underscores. It may look like the __dummyPrivateMethod below. You can feel
# free to change any of the class attributes, as long as you do not change any
# of the given function headers (they must take and return the same arguments).

class KNNModel:
    def __init__(self, k):
        self.X = None
        self.y = None
        self.K = k

    # Just to show how to make 'private' methods
    def __dummyPrivateMethod(self, input):
        return None

    def __calcDist(self, mag1, mag2, temp1, temp2):
        return ((mag1 - mag2) / 3) ** 2 + (temp1 - temp2) ** 2

    # TODO: Implement this method!
    def predict(self, X_pred):
        # The code in this method should be removed and replaced! We included it
        # just so that the distribution code is runnable and produces a
        # (currently meaningless) visualization.
        preds = []
        for x in X_pred:
            dist = []
            for pt in range(len(self.X)):
                dist.append((self.__calcDist(x[0], self.X[pt][0], x[1], self.X[pt][1]), self.y[pt]))
            
            sorted_dist = sorted(dist, key=lambda y : y[0])

            prediction = []
            for i in range(self.K):
                prediction.append(sorted_dist[i][1])

            preds.append(np.bincount(np.array(prediction)).argmax())

        return np.array(preds)

    # In KNN, "fitting" can be as simple as storing the data, so this has been written for you
    # If you'd like to add some preprocessing here without changing the inputs, feel free,
    # but it is completely optional.
    def fit(self, X, y):
        self.X = X
        self.y = y