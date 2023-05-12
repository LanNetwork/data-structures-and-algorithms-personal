from collections import deque 


class IslandCounterClass:
  """...write comment for this class..."""


  def __init__(self, grid):
    """...write comment about this method...

    Parameters
    ----------
    grid : 2d-array
        describe...
    """
    self.grid = grid
    self.visited = [['0' for x in range(len(grid[0]))] for y in range(len(grid))]
  

  def print_grid_visited(self):
    """...write comment about this method...
    """
    print("Map:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.grid]))
    print("Visited:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.visited]))


  def count_island(self):
    """...write comment about this method...

    Returns
    -------
    result
        ...
    """
    result = 0

    for x in range(len(self.grid)):
      for y in range(len(self.grid[0])):
        if self.grid[x][y] == "1" and self.visited[x][y] == "0": # land ho, begin the bfs
          result += 1
          self.mark_visited_island(x, y)
    return result
  

  def mark_visited_island(self, x, y):
    """...write comment about this method...

    Parameters
    ----------
    x : integer
        describe...
    y : integer
        describe...
    """ 
    queue_x = deque() 
    queue_y = deque()
    
    queue_x.append(x)
    queue_y.append(y)
    while queue_x: #run through this and populate queues until they're empty.
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
