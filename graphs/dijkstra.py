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

    def add_vertex_data(self, vertex: int, name: str) -> None:
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = name

    def shortest_path(self, start_vertex):
        """
        Implementation of Dijkstra's shortest path algorithm
        """
        distances = [float('inf')] * self.size
        start_vertex_index = self.vertex_data.index(start_vertex)
        distances[start_vertex_index] = 0
        visited = [False] * self.size


class ShortestPathTest(unittest.TestCase):

    def test_single_route(self):
        graph = Graph(1)
        graph.add_vertex_data(0, 'A')
        graph.add_vertex_data(1, 'B')
        graph.add_edge(0, 1, 10)


if __name__ == '__main__':
    unittest.main()
