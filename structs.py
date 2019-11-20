class Node:

    def __init__(self, name, neighbors=None, rank=1.0):
        if neighbors is None:
            neighbors = []
        self.name = name
        self.neighbors = neighbors
        self.rank = rank

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def add_neighbors(self, neighbors):
        self.neighbors.extend(neighbors)
