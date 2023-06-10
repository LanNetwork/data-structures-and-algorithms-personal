from collections import deque


class IslandCounterClass:
    """Class for handling maps of islands"""

    def __init__(self, grid):
        """Initializes an IslandCounterClass with a passed grid.

        Parameters
        ----------
        grid : 2d-array
            2d-array made up of strings, either "1" or "0"
        """
        self.grid = grid
        self.visited = [['0' for x in range(len(grid[0]))]
                        for y in range(len(grid))]

    def print_grid_visited(self):
        """Prints a map of the visited land tiles. 1 is visited land, 0 is water.
        """
        print("Map:")
        print('\n'.join(['\t'.join([str(cell) for cell in row])
              for row in self.grid]))
        print("Visited:")
        print('\n'.join(['\t'.join([str(cell) for cell in row])
              for row in self.visited]))

    def count_island(self):
        """Counts the number of islands in the passed grid.
        An island is a body of land adjacent land tiles (no diagonals).

        Returns
        -------
        result
            An int representing how many islands are present in self.grid.
        """
        result = 0

        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y] == "1" and self.visited[x][y] == "0":  # land ho, begin the bfs
                    result += 1
                    self.mark_visited_island(x, y)
        return result

    def mark_visited_island(self, x, y):
        """Uses depth first search to mark all land tiles.
        This function has no awareness of if the tile at x and y have been checked on not,
          so handle that outside of this function.

        Parameters
        ----------
        x : integer
            x coordinate to begind check on.
        y : integer
            y coordinate to begind check on.
        """
        queue_x = deque()
        queue_y = deque()

        queue_x.append(x)
        queue_y.append(y)
        while queue_x:  # run through this and populate queues until they're empty.
            x = queue_x.popleft()
            y = queue_y.popleft()
            self.visited[x][y] = "1"
            # check up
            up = x - 1
            # if in bounds, and not visited, and grid value == '1', enqueue
            if (up >= 0 and up < len(self.grid)) and (self.visited[up][y] == "1") and (self.grid[up][y] == "0"):
                queue_x.append(up)
                queue_y.append(y)

            # check down
            down = x + 1
            # if in bounds, and not visited, and grid value == '1', enqueue
            if (down >= 0 and down < len(self.grid)) and (self.visited[down][y] == "0") and (self.grid[down][y] == "1"):
                queue_x.append(down)
                queue_y.append(y)

            # check left
            left = y - 1
            # if in bounds, and not visited, and grid value == '1', enqueue
            if (left >= 0 and left < len(self.grid[0])) and (self.visited[x][left] == "0") and (self.grid[x][left] == "1"):
                queue_x.append(x)
                queue_y.append(left)

            # check right
            right = y + 1
            # if in bounds, and not visited, and grid value == '1', enqueue
            if (right >= 0 and right < len(self.grid[0])) and (self.visited[x][right] == "0") and (self.grid[x][right] == "1"):
                queue_x.append(x)
                queue_y.append(right)

            # now that we've enqueued all the valid options, we are done. Goodbye.
