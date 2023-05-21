class DijkstraClass:
    """...write comment for this class..."""

    def __init__(self, graph: dict):
        """
        Initializes a hashmap representation of a weighted directed graph. Expects only positive weights.
        This class has methods related to Dijkstra's shortest path algorithm.
        Always tries to finds path from node 's' to 'f'.
        Parameters
        ----------
        grid : hash graph map
            Hashmap representation of weighted directed graph. Positive weights only.
        """
        # graph to be compute shortest path
        self.graph = graph

        # define infinity to be used through out class
        self.infinity: float = float("inf")

        # define known/computed costs to node
        self.costs = {}

        # define parts of each node in the beginning or at each moment
        self.parents = {}

        # used if this node have been processed
        self.processed = []

    def initial_costs_parents(self):
        """This method initializes costs and parents global variables as to how the Dijkstra algorithm works."""
        for node in self.graph.keys():
            self.costs[node] = self.infinity
            self.parents[node] = {}
        self.costs['s'] = 0

    def find_shorted_path(self):
        """This method updates costs and parents global variables by following the Dijkstra algorithm."""

        node = self.find_lowest_cost_node()
        for


    def find_lowest_cost_node(self):
        """
        This method finds and returns the lowest cost node that hasn't been processed yet.
        Parameters: costs
        """
        lowest_cost = self.infinity
        lowest_cost_node = None

        for node in self.costs.keys():
            if node not in self.processed:
                if self.costs[node] <= lowest_cost:
                    lowest_cost = self.costs[node]
                    lowest_cost_node = node
        return lowest_cost_node

    def print_path(self):
        """If there is path, prints path from's' to 'f'."""
        # TODO: function logic
        path = []
        print(path)
