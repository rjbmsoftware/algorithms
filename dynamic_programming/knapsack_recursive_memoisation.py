import unittest


def knapsack(weights: list[int], values: list[int], capacity: int,
             weight_value_cache: list[list[int]], index: int):
    return 1


def knapsack_cache(values: list[tuple[int, int]], capacity: int) -> list[list[int]]:
    capacity += 1
    return [[0] * capacity for _ in range(len(values))]


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
