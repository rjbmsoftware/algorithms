import unittest

def knapsack_optimiser(items: list[tuple[int, int]], capacity: int) -> list[tuple[int, int]]:
    """
    Work out which items for a given weight, value, and knapsack capacity have the highest
    overall value
    """
    capacities = [0] * capacity
    items_by_capacities = [capacities] * (len(items) + 1)
    return []

class KnapsackTest(unittest.TestCase):

    def test_empty_items_empty_knapsack(self):
        items = knapsack_optimiser([], 99)
        self.assertFalse(items)

if __name__ == "__main__":
    unittest.main()
