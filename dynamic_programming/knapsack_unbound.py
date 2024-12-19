import unittest

def knapsack_unbound(weights, values, capacity):
    """
    Unbound knapsack problem

    steps

    complexity:
        time:
        space:
    """
    for i in range(len(weights)):
        pass


class KnapsackUnboundTest(unittest.TestCase):
    def test_all_items_fit(self):
        weights = [1, 2, 3]
        values = [10, 15, 40]
        capacity = 6
        value = knapsack_unbound(weights, values, capacity)
        self.assertEqual(value, 65)

    def test_two_of_three_items_fit(self):
        weights = [1, 3, 3]
        values = [10, 15, 40]
        capacity = 6
        value = knapsack_unbound(weights, values, capacity)
        self.assertEqual(value, 55)

    def test_no_items_fit(self):
        weights = [9, 7]
        values = [15, 40]
        capacity = 6
        value = knapsack_unbound(weights, values, capacity)
        self.assertEqual(value, 0)

if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':
    unittest.main()
