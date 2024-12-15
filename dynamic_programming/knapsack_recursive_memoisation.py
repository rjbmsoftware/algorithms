import unittest

def knapsack(items, capacity, cache, index = 0):

    if capacity <= 0 or index >= len(items):
        return 0

    weight, value = items[index]

    with_item_value = 0
    if weight <= capacity:
        with_item_value = value

    next_index = index + 1

    return max(
        with_item_value + knapsack(items, capacity - weight, cache, next_index),
        knapsack(items, capacity, cache, next_index)
    )

def knapsack_cache(items: list[tuple[int, int]], capacity: int) -> list[list[int]]:
    return [[0] * capacity for _ in range(len(items))]


class KnapsackTest(unittest.TestCase):
    def test_all_items_fit(self):
        items = [(1, 10), (2, 15), (3, 40)]
        capacity = 6
        cache = knapsack_cache(items, capacity)
        value = knapsack(items, capacity, cache)
        self.assertEqual(value, 65)

    def test_two_of_three_items_fit(self):
        items = [(1, 10), (3, 15), (3, 40)]
        capacity = 6
        cache = knapsack_cache(items, capacity)
        value = knapsack(items, capacity, cache)
        self.assertEqual(value, 55)

    def test_no_items_fit(self):
        items = [(9, 15), (7, 40)]
        capacity = 6
        cache = knapsack_cache(items, capacity)
        value = knapsack(items, capacity, cache)
        self.assertEqual(value, 0)

if __name__ == "__main__":
    unittest.main()
