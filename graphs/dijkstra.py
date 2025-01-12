import unittest


class Graph:
    def __init__(self, size: int):
        """
        Undirected graph
        """
        self.adjacency_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_names = [''] * size

    def add_edge(self, u: int, v: int, weight: int) -> None:
        self.adjacency_matrix[u][v] = weight
        self.adjacency_matrix[v][u] = weight

    def set_vertex_name(self, vertex: int, name: str) -> None:
        if 0 <= vertex < self.size:
            self.vertex_names[vertex] = name

    def shortest_distance(self, start_vertex_name: str) -> list[float]:
        """
        Implementation of Dijkstra's shortest path algorithm
        """
        distances = [float('inf')] * self.size
        start_vertex_index = self.vertex_names.index(start_vertex_name)
        distances[start_vertex_index] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            minimum_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < minimum_distance:
                    minimum_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adjacency_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adjacency_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances


class ShortestPathTest(unittest.TestCase):

    def test_single_route(self):
        graph = Graph(2)
        graph.set_vertex_name(0, 'A')
        graph.set_vertex_name(1, 'B')
        graph.add_edge(0, 1, 10)

        distances = graph.shortest_distance('A')
        self.assertEqual(distances[0], 0)
        self.assertEqual(distances[1], 10)


if __name__ == '__main__':
    unittest.main()
