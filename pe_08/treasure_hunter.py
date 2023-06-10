class TreasureHunterClass:
    """...write comment for this class..."""

    def __init__(self):
        """I'm not really sure I need to initialize anything."""
        pass

    
    def hunt_treasure(self, arr, n, k): 
        """Makes each hunter hunt for treasure. Returns the maximum amount of treasure than can be found
        with the particular set of hunters.
        """

        # Define a set to store visited indexes of arr.
        captured = set()
        count = 0

        # Iterate arr until you hit hunter. Then, check k units in front of the hunter for non-captured treasure.
        for i in range(len(arr)):
            if arr[i] == 'H':
                for j in range(i-k, i+k): # Check items in range of current hunter, starting as far left as possible.
                    # Make sure j is in bounds.
                    if j < 0: # too small, next iteration
                         continue
                    elif j > len(arr) - 1: # too large, quit loop.
                         break
                    else: # in range.
                        if (arr[j] == 'T') and (not (j in captured)): # check if it's a valid treasure
                                captured.add(j)
                                count += 1
                                break
        return count