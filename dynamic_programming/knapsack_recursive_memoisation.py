import unittest


def knapsack(weights: list[int], values: list[int], capacity: int,
             weight_value_cache: list[list[int]], index: int):
    """
    Recursive memoised solution

    complexity
        time:
            0(n * m) as the cache of values is filled
        space:
            0(n * m + n) where n is the amount of items and m the capacity for the cached
            values and an additional n for the maximum height of recursive call stack
    """
    if index < 0:
        return 0

    if weight_value_cache[index][capacity] != -1:
        return weight_value_cache[index][capacity]

    if weights[index] > capacity:
        weight_value_cache[index][capacity] = knapsack(
            weights, values, capacity, weight_value_cache, index - 1)
    else:
        weight_value_cache[index][capacity] = max(
            knapsack(weights, values, capacity, weight_value_cache, index - 1),
            values[index] + knapsack(weights, values,
                                     capacity - weights[index], weight_value_cache, index - 1),
        )

    return weight_value_cache[index][capacity]


def knapsack_cache(values: list[tuple[int, int]], capacity: int) -> list[list[int]]:
    capacity += 1
    return [[-1] * capacity for _ in range(len(values))]


class KnapsackTest(unittest.TestCase):
    def test_all_items_fit(self):
        weights = [1, 2, 3]
        values = [10, 15, 40]
        index = len(values) - 1
        capacity = 6
        cache = knapsack_cache(values, capacity)
        value = knapsack(weights, values, capacity, cache, index)
        self.assertEqual(value, 65)

    def test_two_of_three_items_fit(self):
        weights = [1, 3, 3]
        values = [10, 15, 40]
        index = len(values) - 1
        capacity = 6
        cache = knapsack_cache(values, capacity)
        value = knapsack(weights, values, capacity, cache, index)
        self.assertEqual(value, 55)

    def test_no_items_fit(self):
        weights = [9, 15]
        values = [15, 40]
        index = len(values) - 1
        capacity = 6
        cache = knapsack_cache(values, capacity)
        value = knapsack(weights, values, capacity, cache, index)
        self.assertEqual(value, 0)


if __name__ == "__main__":
    unittest.main()
