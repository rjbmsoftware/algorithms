import unittest


def insertion_sort(values: list) -> None:
    # TODO: split out is sorted method
    # TODO: write up solution, comparison of shift vs swap
    for working_index in range(1, len(values)):
        current_value = values[working_index]
        backwards_index = working_index
        while backwards_index > 0 and values[backwards_index - 1] > current_value:
            values[backwards_index] = values[backwards_index - 1]
            backwards_index -= 1
        values[backwards_index] = current_value


def swap(values: list, first_index: int, second_index: int) -> None:
    values[first_index], values[second_index] = values[second_index], values[first_index]


class InsertionSortTest(unittest.TestCase):

    def is_sorted(self, input: list) -> bool:
        """
        returns if the list is sorted
        """
        if len(input) <= 1:
            return True

        i = 0
        max_index = len(input) - 1
        while i < max_index:
            if input[i] > input[i + 1]:
                return False

            i += 1

        return True

    def test_empty_list(self):
        values = []
        insertion_sort(values)
        self.assertEqual(values, [])

    def test_single_value_list(self):
        values = [1]
        insertion_sort(values)
        self.assertEqual(len(values), 1)
        self.assertTrue(values[0], 1)

    def test_two_value_list(self):
        values = [2, 1]
        insertion_sort(values)
        self.assertTrue(self.is_sorted(values),
                        f'Expected [1, 2], actual {values}')

    def test_three_value_list(self):
        values = [3, 2, 1]
        insertion_sort(values)
        self.assertTrue(self.is_sorted(values),
                        f'Expected [1, 2, 3], actual {values}')

    def test_max_to_min(self):
        input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_sort(input)
        self.assertTrue(self.is_sorted(input))

    def test_empty_is_sorted(self):
        input = []
        insertion_sort(input)
        self.assertTrue(self.is_sorted(input))

    def test_already_sorted(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        insertion_sort(input)
        self.assertTrue(self.is_sorted(input))

    def test_same(self):
        input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        insertion_sort(input)
        self.assertTrue(self.is_sorted(input))


if __name__ == "__main__":
    unittest.main()
