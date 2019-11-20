class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.rank = 1.0

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def add_neighbors(self, neighbors):
        self.neighbors.extend(neighbors)
