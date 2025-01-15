from collections import defaultdict
import unittest


class Graph:
    def __init__(self, size: int):
        """
        Undirected graph
        """
        # self.adjacency_matrix = [[0] * size for _ in range(size)]
        self.adjacency_list: defaultdict[int, dict[int, int]] = defaultdict(dict)
        self.size = size
        self.vertex_names = [''] * size

    def add_edge(self, u: int, v: int, weight: int) -> None:
        # self.adjacency_matrix[u][v] = weight
        # self.adjacency_matrix[v][u] = weight
        # from_index = self.vertex_names[u]
        # to_index = self.vertex_names[v]
        # self.adjacency_list[from_index][to_index] = weight
        # self.adjacency_list[to_index][from_index] = weight
        self.adjacency_list[u][v] = weight
        self.adjacency_list[v][u] = weight

    def set_vertex_name(self, vertex: int, name: str) -> None:
        if 0 <= vertex < self.size:
            self.vertex_names[vertex] = name

    def shortest_distance(self, start_vertex_name: str) -> list[float]:
        """
        Implementation of Dijkstra's shortest path algorithm

        steps
            # create an adjacency matrix add relevant weights to the edges
            create a list of distances set to infinite and the starting point to zero
            create a list of vertex visited status set to false
            loop over the individual lists in the adjacency matrix finding the minimum distance
            break if unreachable
            loop over the individual lists in the adjacency matrix if not visited and not the
            starting vertex compare the distances saving the minimum

            output is a list of minimum distance to the respective vertex

            Complexity:
                time: O(n squared) where n is amount of vertices as the worst case there will be an
                edge from each vertex to all other vertices which will have to visited and checked.

                space: O(n squared) where n is the amount of vertices as the adjacency matrix will
                need to record edges from each vertex to all other vertices.
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

            # for v in range(self.size):
            #     if self.adjacency_list[u][v] != 0 and not visited[v]:
            #         alt = distances[u] + self.adjacency_list[u][v]
            #         if alt < distances[v]:
            #             distances[v] = alt

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

    def test_diamond(self):
        graph = Graph(4)
        graph.set_vertex_name(0, 'A')
        graph.set_vertex_name(1, 'B')
        graph.set_vertex_name(2, 'C')
        graph.set_vertex_name(3, 'D')

        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 3)
        graph.add_edge(1, 3, 1)
        graph.add_edge(2, 3, 1)

        distances = graph.shortest_distance('A')
        self.assertEqual(distances[3], 2)


if __name__ == '__main__':
    unittest.main()
