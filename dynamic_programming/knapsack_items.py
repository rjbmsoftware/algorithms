import unittest


def knapsack_grid(items: list[tuple[int, int]], total_capacity) -> list[list[int]]:
    """
    knap sack problem solver finding the best items to take
    items is a list of tuples of the item weight and value

    iterative bottom up solution
    create an 2d array initialising them all to zero
    leaving the left most column and top row as zeros
    iterate through the items and capacities
    
    if the item fits and its value higher than the row above for the given capacity
    the stored value is the item value plus the above row for the remaining capacity
    else store the above row value for the current capacity
    """

    items_by_capacities = [[0] * (total_capacity + 1)
                           for _ in range(len(items) + 1)]

    for item_index in range(1, len(items_by_capacities)):
        for capacity in range(1, total_capacity + 1):
            weight, value = items[item_index - 1]
            if weight <= capacity and value > items_by_capacities[item_index - 1][capacity]:
                new_value = value + \
                    items_by_capacities[item_index - 1][capacity - weight]
            else:
                new_value = items_by_capacities[item_index - 1][capacity]

            items_by_capacities[item_index][capacity] = new_value

    return items_by_capacities


def knapsack_which_items(items: list[tuple[int, int]], matrix:list[list[int]]) -> list[tuple[int, int]]:
    """
    Find out which items have been packed by back tracking through
    the matrix and items

    steps
        work backwards through the items lists comparing the
        values in the matrix at the items weight with the row
        above, if they are not equal the item was packed.

    complexity
        time:
            O(n) where n is the amount of items that could be
            packed as each item gets compared with weighted value
            in the matrix.
        space:
            O(n) where n is the amount of items that could be
            packed as a list of items is returned the worst case
            being they all fit in the knapsack
    """
    taken_items = []
    for i in range(len(items) - 1, -1, -1):
        weight = items[i][0]
        item_fits_in_knapsack = weight < len(matrix[0])
        if item_fits_in_knapsack:
            old_value = matrix[i][weight -1]
            new_value = matrix[i + 1][weight +1]
            item_packed = old_value != new_value
            if item_packed:
                taken_items.append(items[i])

    taken_items.reverse()
    return taken_items


class KnapSackItemsTest(unittest.TestCase):

    def test_all_items_included(self):
        items = [(1, 10), (2, 15), (3, 40)]
        capacity = 6
        grid = knapsack_grid(items, capacity)
        taken_items = knapsack_which_items(items, grid)
        self.assertEqual(items, taken_items)

    def test_two_of_three_items_fit(self):
        items = [(1, 10), (3, 15), (3, 40)]
        capacity = 6
        grid = knapsack_grid(items, capacity)
        taken_items = knapsack_which_items(items, grid)
        self.assertEqual(len(taken_items), 2)

    def test_no_items_included_empty_list(self):
        items = [(9, 15), (7, 40)]
        capacity = 6
        matrix = knapsack_grid(items, capacity)
        taken_items = knapsack_which_items(items, matrix)
        self.assertFalse(taken_items)


class KnapsackGridTest(unittest.TestCase):

    def test_all_items_fit(self):
        items = [(1, 10), (2, 15), (3, 40)]
        capacity = 6
        grid = knapsack_grid(items, capacity)
        self.assertEqual(grid[-1][-1], 65)

    def test_two_of_three_items_fit(self):
        items = [(1, 10), (3, 15), (3, 40)]
        capacity = 6
        grid = knapsack_grid(items, capacity)
        self.assertEqual(grid[-1][-1], 55)

    def test_no_items_fit(self):
        items = [(9, 15), (7, 40)]
        capacity = 6
        grid = knapsack_grid(items, capacity)
        self.assertEqual(grid[-1][-1], 0)


if __name__ == '__main__':
    unittest.main()
