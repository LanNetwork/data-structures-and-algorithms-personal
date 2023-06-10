class LCSClass:
    """Containter class for calculating length of longest common substring between two strings."""

    def __init__(self):
        """Initializes class. Does this need to be here?"""
        pass

    def find(self, x, y):
        """Returns the length of the longest common subsequence between x and y."""
        m, n = len(x), len(y)
        compareGrid = [[0] * (n + 1) for _ in range(m + 1)]
        # print(compareGrid)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, increment length of LCS in grid.
                if x[i - 1] == y[j - 1]:
                    compareGrid[i][j] = compareGrid[i-1][j-1] + 1
                # Else, characters don't match and take max LCS length.
                else:
                    compareGrid[i][j] = max(compareGrid[i-1][j], compareGrid[i][j-1])

    # bottom right corner is LCS length.
        return compareGrid[m][n]
