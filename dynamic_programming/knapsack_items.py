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


def knapsack_which_items(items: list[tuple[int, int]], total_capacity, matrix:list[list[int]]) -> list[tuple[int, int]]:
    
    taken_items = []
    for i in range(total_capacity, 0, -1):
        
     
    return taken_items


class KnapSackItemsTest(unittest.TestCase):

    def test_no_items_included_empty_list(self):
        items = [(9, 15), (7, 40)]
        capacity = 6
        matrix = knapsack_grid(items, capacity)
        taken_items = knapsack_which_items(items, capacity, matrix)
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
