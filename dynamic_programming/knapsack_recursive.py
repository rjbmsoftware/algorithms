import unittest

def knapsack(items, capacity):

    if capacity <= 0 or not items:
        return 0

    weight, value = items[0]
    items = items[1:]

    with_item_value = 0
    if weight <= capacity:
        with_item_value = value

    return max(
        with_item_value + knapsack(items, capacity - weight),
        knapsack(items, capacity)
    )


class KnapsackTest(unittest.TestCase):
    def test_all_items_fit(self):
        items = [(1, 10), (2, 15), (3, 40)]
        capacity = 6
        value = knapsack(items, capacity)
        self.assertEqual(value, 65)

    def test_two_of_three_items_fit(self):
        items = [(1, 10), (3, 15), (3, 40)]
        capacity = 6
        value = knapsack(items, capacity)
        self.assertEqual(value, 55)

    def test_no_items_fit(self):
        items = [(9, 15), (7, 40)]
        capacity = 6
        value = knapsack(items, capacity)
        self.assertEqual(value, 0)

if __name__ == "__main__":
    unittest.main()
