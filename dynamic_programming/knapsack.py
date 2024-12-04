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
    items_by_capacities = []
    for _ in range(len(items) + 1):
        items_by_capacities.append([0] * (total_capacity + 1))
    for i in range(1, len(items_by_capacities)):
        for j in range(1, total_capacity + 1):
            weight, value = items[i - 1]
            if weight <= j and value > items_by_capacities[i - 1][j]:
                items_by_capacities[i][j] = value + \
                    items_by_capacities[i - 1][j - weight]
            else:
                items_by_capacities[i][j] = items_by_capacities[i - 1][j]
    for items_by_capacity in items_by_capacities:
        print(items_by_capacity)
    return []


class KnapsackTest(unittest.TestCase):

    # def test_empty_items_empty_knapsack(self):
    #     items = knapsack_optimiser([], 99)
    #     self.assertFalse(items)

    def test_example(self):
        # Let, weight[] = {1, 2, 3}, profit[] = {10, 15, 40}, Capacity = 6
        items = [(1, 10), (2, 15), (3, 40)]
        capacity = 6
        output = knapsack_optimiser(items, capacity)


if __name__ == "__main__":
    unittest.main()
