import unittest


class Graph:
    def __init__(self, size: int):
        """
        Undirected graph
        """
        self.adjacency_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u: int, v: int, weight: int) -> None:
        self.adjacency_matrix[u][v] = weight
        self.adjacency_matrix[v][u] = weight

    def add_vertex_data(self, vertex: int, data: list[int]) -> None:
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

def shortest_path():
    """
    Implementation of Dijkstra's shortest path algorithm
    """


class ShortestPathTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
