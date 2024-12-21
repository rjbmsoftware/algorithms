import unittest


def knapsack_unbound(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Unbound knapsack problem

    steps

    complexity:
        time:
        space:
    """
    cache_capacity = capacity + 1
    value_cache = [[-1] * cache_capacity for _ in weights]

    knapsack_cache_filler(weights, values, capacity,
                          value_cache, len(weights) - 1)

    return value_cache[-1][-1]


def knapsack_cache_filler(weights, values, capacity, cache, index):
    """
    Recursive function to fill the cache for unbounded knapsack.
    """
    if index < 0 or capacity < 0 or cache[index][capacity] != -1:
        return

    if capacity == 0:
        cache[index][capacity] = 0
        return

    knapsack_cache_filler(weights, values, capacity,
                          cache, index - 1)  # Skip item
    if weights[index] <= capacity:
        knapsack_cache_filler(weights, values, capacity -
                              weights[index], cache, index)  # Take item

    skip_value = cache[index - 1][capacity] if index > 0 else 0
    take_value = values[index] + cache[index][capacity -
                                              weights[index]] if weights[index] <= capacity else 0

    cache[index][capacity] = max(skip_value, take_value)


class KnapsackUnboundTest(unittest.TestCase):
    def test_all_items_fit(self):
        weights = [1, 2, 3]
        values = [10, 15, 40]
        capacity = 6
        value = knapsack_unbound(weights, values, capacity)
        self.assertEqual(value, 80)

    def test_two_of_three_items_fit(self):
        weights = [1, 3, 4]
        values = [10, 55, 40]
        capacity = 6
        value = knapsack_unbound(weights, values, capacity)
        self.assertEqual(value, 110)

    def test_no_items_fit(self):
        weights = [9, 7]
        values = [15, 40]
        capacity = 6
        value = knapsack_unbound(weights, values, capacity)
        self.assertEqual(value, 0)

    def test_two_of_one_one_of_another(self):
        weights = [1, 2, 3, 4]
        values = [10, 90, 55, 40]
        capacity = 5
        value = knapsack_unbound(weights, values, capacity)
        self.assertEqual(value, 190)

    def test_left_over_capacity(self):
        weights = [2, 3, 4]
        values = [90, 55, 40]
        capacity = 5
        value = knapsack_unbound(weights, values, capacity)
        self.assertEqual(value, 180)


if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':
    unittest.main()
