from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.metrics import accuracy_score
import pandas as pd
import csv


class knnWrapperClass:
    def __init__(self):
        self.knn = None
        self.df_train = None
        self.df_train_target = None
        self.df_test = None
        self.df_test_target = None
        self.predicted_values = None

    def train(self, neighbors):
        """Train the k-nearest neighbors classifier.

        Args:
            neighbors (int): The number of neighbors to consider.

        """
        self.knn = KNeighborsClassifier(n_neighbors=neighbors)
        self.knn.fit(self.df_train, self.df_train_target)

    def predict(self):
        """Predict the classes of the test data.

        Returns:
            numpy.ndarray: The predicted classes.

        """
        self.predicted_values = self.knn.predict(self.df_test)
        return self.predicted_values

    def import_train_file(self, trainDataFile, trainTargetFile):
        """Import the training data and target CSV file.

        Args:
            trainDataFile (str): The filename of the training data CSV file.
            trainTargetFile (str): The filename of the training target CSV file.

        """
        self.df_train = pd.read_csv(trainDataFile)
        self.df_train_target = pd.read_csv(trainTargetFile)

    def import_test_file(self, testDataFile, testTargetFile):
        """Import the test data and target CSV file.

        Args:
            testDataFile (str): The filename of the test data CSV file.
            testTargetFile (str): The filename of the test target CSV file.

        """
        self.df_test = pd.read_csv(testDataFile)
        self.df_test_target = pd.read_csv(testTargetFile)

    def accuracy(self):
        """Return accuracy difference between predicted and actual labels.

        Returns:
            int: accuracy rating        
        """
        return accuracy_score(self.predicted_values, self.df_test_target)