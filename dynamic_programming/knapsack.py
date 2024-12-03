import unittest

def knapsack_optimiser(items: list[tuple[int, int]], total_capacity: int) -> list[tuple[int, int]]:
    """
    Work out which items for a given weight, value, and knapsack capacity have the highest
    overall value
    
    complexity:
        time:

        space:

    Bottom up iterative approach

    """
    capacities = [0] * total_capacity
    items_by_capacities = [capacities] * (len(items) + 1)
    for capacity in range(1, len(items)):
        for item in range(capacities[capacity]):
            weight, value = items[capacity]
            if weight < j:

            items_by_capacities[capacity][j]
    return []

class KnapsackTest(unittest.TestCase):

    def test_empty_items_empty_knapsack(self):
        items = knapsack_optimiser([], 99)
        self.assertFalse(items)

if __name__ == "__main__":
    unittest.main()
