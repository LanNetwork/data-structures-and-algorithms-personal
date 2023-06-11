"""knn_wrapper_main.py

This assignment is to learn about k-nearest neighbors.
Given two data sets, complete the functions in the separate "knnWrapperClass" class within knn_wrapper.py,
and edit the parameter on the "train" method call from the main method to achieve 100% accuracy.
The "knnWrapperClass" object is to implement a k-nearest classifier wrapper and classify test data.
Note that you are allowed to use the KNeighborsClassifier library from sklearn, and you need to achieve a 100% classification rate on test data.
In short paragraph, provide which 'neighbor' parameter works best for each dataset and describe tips on choosing the 'neighbor' value.

-Files are in pair of "data" and "target," where their lows are synced, and each data low is labeled with classes at the target file.
  Train files: iris_data.csv, iris_target.csv, wine_data.csv, wine_target.csv
  Test files: iris_test_data.csv, iris_test_target.csv, wine_test_data.csv, wine_test_target.csv

-Result should achieve five 0s, five 1s, five 2s:
  [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]
  [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]


"""

""" IAN MCGEOY STUDENT ANSWER:
    n value of 1 worked best for both datasets. I would reccomend automating the selection of an n value,
    because now that I have a function to do that, you can use it any time you're using a knn model.
    """
from knn_wrapper import knnWrapperClass


def main():
    
    best_n, best_acc = find_best_n(("iris_data.csv", "iris_target.csv"), ("iris_test_data.csv", "iris_test_target.csv"))
    # print(f'Best n: {best_n}\nAcc: {best_acc}')
    knnW = knnWrapperClass()
    knnW.import_train_file("iris_data.csv", "iris_target.csv")
    # have set neighbor n value as 2, but please find better value
    print(f'Using n = {best_n}')
    knnW.train(best_n)
    knnW.import_test_file("iris_test_data.csv", "iris_test_target.csv")
    result = knnW.predict()
    print(result)

    best_n, best_acc = find_best_n(("wine_data.csv", "wine_target.csv"), ("wine_test_data.csv", "wine_test_target.csv"))
    # print(f'Best n: {best_n}\nAcc: {best_acc}')
    knnW = knnWrapperClass()
    knnW.import_train_file("wine_data.csv", "wine_target.csv")
    print(f'Using n = {best_n}')
    knnW.train(best_n)
    knnW.import_test_file("wine_test_data.csv", "wine_test_target.csv")
    result = knnW.predict()
    print(result)


def find_best_n(training_data: tuple, testing_data: tuple, starting_n: int = 1, limit: int = 15):
    # This function tests the knn wrapper on it's imported datasets with different values
    # of n, until either accuracy == 1, or limit is met.
    best_n = None
    best_accuracy = 0
    for n in range(starting_n, limit):
        knn = knnWrapperClass()
        knn.import_train_file(training_data[0], training_data[1])
        knn.import_test_file(testing_data[0], testing_data[1])
        knn.train(n)
        knn.predict()
        acc = knn.accuracy()
        if acc > best_accuracy:
            best_n = n
            best_accuracy = acc
            if best_accuracy == 1:
                break
    return (best_n, best_accuracy)


if __name__ == "__main__":
    main()
