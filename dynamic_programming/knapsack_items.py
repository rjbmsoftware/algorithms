import unittest

def knapsack_best_items(items: list[tuple[int, int]], capacity) -> list[tuple[int, int]]:
    """
    knap sack problem solver finding the best items to take
    """

class KnapsackTest(unittest.TestCase):

    def test_empty_items(self):
        items = []
        capacity = 10
        packed_items = knapsack_best_items(items, capacity)
        self.assertFalse(packed_items)

if __name__ == '__main__':
    unittest.main()
