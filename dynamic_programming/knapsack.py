import unittest


def knapsack_optimiser(items: list[tuple[int, int]], total_capacity: int) -> int:
    """
    Calculate for a list of items with a given weight, value and capacity
    what is largest value overall value we can have.

    steps
        create a 2D array of the capacity + 1 by the length of items + 1
        filling the array with zeros, first row and column are used as
        reference values.

        for each item calculate if the item will fit plus the value of
        the remaining capacity from the row above and that value is
        greater than the value to the left of the current value.

    complexity:
        time:
            O(nm) where n is the number of items and m is the total
            capacity as the list of lists will be iterated over once
        space:
            O(nm) where n is the number of items and m is the total
            capacity

    Bottom up iterative approach
    """

    items_by_capacities = [[0] * (total_capacity + 1)
                           for _ in range(len(items) + 1)]

    for i in range(1, len(items_by_capacities)):
        for j in range(1, total_capacity + 1):
            weight, value = items[i - 1]
            if weight <= j and value > items_by_capacities[i - 1][j]:
                items_by_capacities[i][j] = value + \
                    items_by_capacities[i - 1][j - weight]
            else:
                items_by_capacities[i][j] = items_by_capacities[i - 1][j]

    return items_by_capacities[-1][-1]


class KnapsackTest(unittest.TestCase):

    def test_all_items_fit(self):
        items = [(1, 10), (2, 15), (3, 40)]
        capacity = 6
        value = knapsack_optimiser(items, capacity)
        self.assertEqual(value, 65)

    def test_two_of_three_items_fit(self):
        items = [(1, 10), (3, 15), (3, 40)]
        capacity = 6
        value = knapsack_optimiser(items, capacity)
        self.assertEqual(value, 55)

    def test_no_items_fit(self):
        items = [(9, 15), (7, 40)]
        capacity = 6
        value = knapsack_optimiser(items, capacity)
        self.assertEqual(value, 0)


if __name__ == "__main__":
    unittest.main()
