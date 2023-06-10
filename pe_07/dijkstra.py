class DijkstraClass:
    """Class for Dijkstra's algorithm implementation"""

    def __init__(self, graph: dict):
        """
        Initializes a hashmap representation of a weighted directed graph. Expects only positive weights.
        This class has methods related to Dijkstra's shortest path algorithm.
        Always tries to find the path from node 's' to 'f'.
        Parameters
        ----------
        graph : dict
            Hashmap representation of a weighted directed graph. Positive weights only.
        """
        self.graph = graph
        self.infinity = float("inf")
        self.costs = {}
        self.parents = {}
        self.processed = []

    def initial_costs_parents(self):
        """Initializes costs and parents global variables as per Dijkstra's algorithm."""
        for node in self.graph.keys():
            self.costs[node] = self.infinity
            self.parents[node] = None
        self.costs['s'] = 0

    def find_shortest_path(self):
        """Updates costs and parents global variables by following Dijkstra's algorithm."""

        node = self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for neighbor in neighbors.keys():
                new_cost = cost + neighbors[neighbor]
                if new_cost < self.costs[neighbor]:
                    self.costs[neighbor] = new_cost
                    self.parents[neighbor] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node()

    def find_lowest_cost_node(self):
        """Finds and returns the lowest cost node that hasn't been processed yet."""
        lowest_cost = self.infinity
        lowest_cost_node = None

        for node in self.costs.keys():
            if node not in self.processed and self.costs[node] <= lowest_cost:
                lowest_cost = self.costs[node]
                lowest_cost_node = node

        return lowest_cost_node

    def print_path(self):
        """If there is a path, prints the path from 's' to 'f'."""
        path = []
        current_node = 'f'
        while current_node != 's':
            path.append(current_node)
            current_node = self.parents[current_node]

            # Check if a valid path exists
            if current_node is None:
                print("No valid path exists from 's' to 'f'.")
                return

        path.append('s')
        path.reverse()
        print(" -> ".join(path))
